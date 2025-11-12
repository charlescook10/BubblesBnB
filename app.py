import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
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
    user_id = 1

    return render_template('list_spaces.html', spaces=spaces, user_id=user_id)

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

# GET /user/spaces/1
# Returns the listings
@app.route('/user/spaces/<int:id>', methods=['GET'])
def get_all_spaces_for_one_user(id):
    conn = get_flask_database_connection(app)
    space_repo = SpaceRepository(conn)
    user_repo = UserRepository(conn)

    spaces = space_repo.find_by_user(id)
    user = user_repo.find(id)
    return render_template('list_spaces_all_of_user.html', users=user, spaces=spaces)


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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
