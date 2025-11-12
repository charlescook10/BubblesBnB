import os
from flask import Flask, request, render_template, redirect, url_for, flash, current_app
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.spaces import Space
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /spaces
# Returns the listings

@app.route("/register", methods=['GET', 'POST'])
def register():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    if request.method == "POST": 
        name = request.form.get("name", "").strip()
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not username or not password: 
            flash("All fields are required", "Error")
            return render_template('register.html')
        if len(password) < 8: 
            flash("Password might be at least 8 characters long")
        
        existing = repo.get_username()
        if username in existing: 
            flash("Username already taken.", "Error")
        
        new_user = User(name=name, username=username, password=password)
        repo.add(new_user)
        flash("Account created. Please login!", "Success")
        return redirect(url_for("login"))
    
    return render_template("register.html")



@app.route('/', methods=['GET'])
def get_spaces():
    conn = get_flask_database_connection(app)
    repo = SpaceRepository(conn)

    spaces = repo.all()

    return render_template('list_spaces.html', spaces=spaces)

@app.route('/approved', methods=['GET'])
def get_approved_booking():

    return render_template('approved.html')

@app.route("/spaces/<int:space_id>")
def get_individual_space(space_id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    user_repo = UserRepository(connection)
    space = space_repo.find(space_id)
    if space is None:
        return ("Not Found", 404)
    user = user_repo.find(space.user_id)
    return render_template("individual_space.html", space=space, user=user)

@app.route('/spaces/<int:id>', methods=['POST'])
def put_booking(id):
    conn = get_flask_database_connection(app)
    repo = SpaceRepository(conn)

    space = repo.find(id)

    if space is None:
        return ("Not Found", 404)

    repo.update(Space(space.id, space.name, space.description, space.price_per_night, True, space.user_id))

    return redirect('/approved')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
