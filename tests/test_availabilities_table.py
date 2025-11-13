import datetime


# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bubbles_bnb.sql")

  

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM availabilities WHERE id= 1")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "date": datetime.date(2025, 8, 11), "status":'Available', "space_id":1 },
    
    ]