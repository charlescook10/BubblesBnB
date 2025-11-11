import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.spaces import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /spaces
# Returns the listings
@app.route('/', methods=['GET'])
def get_spaces():
    conn = get_flask_database_connection(app)
    repo = SpaceRepository(conn)

    spaces = repo.all()

    return render_template('list_spaces.html', spaces=spaces)

@app.route('/approved', methods=['GET'])
def get_approved_booking():

    return render_template('approved.html')

# @app.route('/<int:space_id>')
# def individual_space(space_id):
#     space = get_space(space_id)
#     return render_template('individual_space.html', space=space)

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
