import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
