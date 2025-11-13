import os
from flask import Flask, request, render_template, redirect, url_for, flash, current_app
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
from lib.user_repository import UserRepository

from lib.user import User
from lib.spaces import Space

from lib.availability_repository import AvailabilityRepository

# Create a new Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"] 

class LoginUser(UserMixin):
    def __init__(self, user: User):
        self._user = user
        self.id = str(user.id)
        self.name = getattr(user, "name", "")
        self.username = user.username
        self.password = user.password

    @property
    def domain(self) -> User:
        return self._user

login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id: str):
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    u = repo.find(int(user_id))
    return LoginUser(u) if u else None  
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
            flash("All fields are required", "error")
            return render_template('register.html')
        if len(password) < 8: 
            flash("Password might be at least 8 characters long")

        usernames = repo.all()
        existing = ", ".join([user.username for user in usernames])
        if username in existing: 
            flash("Username already taken.", "error")
        
        pw_hash = generate_password_hash(password)
        new_user = User(id=None, name=name, username=username, password=pw_hash)
        repo.add(new_user)
        flash("Account created. Please login!", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        users = repo.all()
        # find the user object that matches the submitted username
        user = next((u for u in users if u.username == username), None)
        if user and check_password_hash(user.password, password):
            login_user(LoginUser(user))
            flash("Welcome!", "success")
            return redirect(url_for("get_spaces"))
        flash("Invalid username or password!", "error")
    return render_template("login.html")


@app.route('/', methods=['GET'])
def get_spaces():
    conn = get_flask_database_connection(app)
    space_repo = SpaceRepository(conn)
    user_repo = UserRepository(conn)

    spaces = space_repo.all()
    users = user_repo.all()

    return render_template('list_spaces.html', users=users, spaces=spaces)
# Code needs amending with user login details

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

# GET /user/spaces/1
# Returns the listings
@app.route('/user/spaces/<int:user_id>', methods=['GET'])
def get_all_spaces_for_one_user(user_id):
    conn = get_flask_database_connection(app)
    space_repo = SpaceRepository(conn)
    user_repo = UserRepository(conn)

    spaces = space_repo.find_by_user(user_id)
    users = user_repo.find(user_id)
    if spaces is None:
        return ("Not Found", 404)
    return render_template('list_spaces_all_of_user.html', users=users, spaces=spaces)


@app.route('/new_listing', methods=['GET', 'POST'])
def new_listing():
    if request.method == 'GET':
        return render_template('add_new_listings.html')
    else:
        conn = get_flask_database_connection(app)
        repo = SpaceRepository(conn)

        name = request.form['name']
        description = request.form['description']
        price_per_night = float(request.form['price_per_night'])
        user_id = 1

        new_space = Space(
            id=None,
            name=name,
            description=description,
            price_per_night=price_per_night,
            booked_flag=False,
            user_id=user_id
        )

        repo.add_new_listing(new_space)
        return redirect(url_for('get_all_spaces_for_one_user', id=user_id))

    
@app.route('/user/spaces/<int:space_id>/edit', methods=['GET', 'POST'])
def edit_space(space_id):
    conn = get_flask_database_connection(app)
    space_repo = SpaceRepository(conn)
    
    space = space_repo.find(space_id)
    if space is None:
        return ("Not Found", 404)

    if request.method == 'POST':
        # Update space with form data
        space.name = request.form['name']
        space.description = request.form['description']
        space.price_per_night = float(request.form['price_per_night'])
        
        space_repo.update(space)
        return redirect(url_for('get_all_spaces_for_one_user', id=space.user_id))
    
    # GET request: show the form with current details
    return render_template('edit_listing.html', space=space)


@app.route('/user/spaces/<int:user_id>/delete/<int:space_id>', methods=['POST'])
def delete_listing(user_id, space_id):
        conn = get_flask_database_connection(app)
        repo = SpaceRepository(conn)
        repo.delete_space(space_id)
        return redirect(url_for('get_all_spaces_for_one_user', id=user_id))

import datetime 

@app.route('/calender/<int:space_id>', methods=['GET'])
def show_calender(space_id):
        conn = get_flask_database_connection(app)
        repo = SpaceRepository(conn)
        availableRepo = AvailabilityRepository(conn)
        space = repo.find(space_id)
        availability = availableRepo.getAvailableSpaceDates(space_id)
        dates =[dates.date for dates in availability]
        return render_template('calender.html', dates=dates, availabilities = availability)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
