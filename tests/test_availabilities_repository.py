import datetime
from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability

"""
Gets all of the dates using the space_id
"""
def test_get_dates_using_space_id(db_connection):
 db_connection.seed("seeds/bubbles_bnb.sql")
 repo = AvailabilityRepository(db_connection)
 dates = repo.getDates(1)
 assert dates == [Availability(1, datetime.date(2025, 8, 11), 'Booked', 1), Availability(8, datetime.date(2026, 4, 14), 'Booked', 1)]
                  
                  
 
 
 
 





"""
Adding a bunch of dates, given a range
"""

