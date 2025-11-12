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
    result = db_connection.execute("SELECT * FROM availabilities")

    # Assert that the results are what we expect
    assert result == [
        {"id": 1, "date": datetime.date(2025, 8, 11), "status":'Booked', "space_id":1 },
       {"id": 2, "date": datetime.date(2026,1, 1), "status":'Available', "space_id":2 },
       {"id": 3, "date": datetime.date(2025,9, 21), "status":'Booked', "space_id":3 },
       {"id": 4, "date": datetime.date(2026, 2, 1), "status":'Available', "space_id":4 }
       
    ]