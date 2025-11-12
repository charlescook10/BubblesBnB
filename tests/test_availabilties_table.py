# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bubbles_bnb.sql")

  

    # Retrieve all records
    result = db_connection.execute("SELECT * FROM availabilities")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "date": "2025-08-11", "status":'Booked', "space_id":1 },
       {"id": 2, "date": "2026-01-01", "status":'Available', "space_id":2 },
       {"id": 3, "date": "2025-09-21", "status":'Booked', "space_id":3 },
       {"id": 4, "date": "2026-02-01", "status":'Available', "space_id":4 }
       
    ]