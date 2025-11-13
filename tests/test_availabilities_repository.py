import datetime
from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability

"""
#find Gets Availability using the id
"""
def test_get_dates_using_space_id(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = AvailabilityRepository(db_connection)
    date = repo.find(1)
    assert date == Availability(1, datetime.date(2025, 8, 11), 'Available', 1) 

"""
Gets all of the dates using the space_id
"""
def test_get_dates_using_space_id(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = AvailabilityRepository(db_connection)
    dates = repo.getSpaceDates(1)
    assert dates == [Availability(1, datetime.date(2025, 8, 11), 'Available', 1), Availability(8, datetime.date(2026, 4, 14), 'Booked', 1)]    

"""
Gets all of the available dates using the space_id
"""
def test_get_dates_using_space_id(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = AvailabilityRepository(db_connection)
    dates = repo.getAvailableSpaceDates(1)
    assert dates == [Availability(1, datetime.date(2025, 8, 11), 'Available', 1)]    

"""
Adding a bunch of dates, given a range
"""
def test_add_dates_in_a_range(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = AvailabilityRepository(db_connection)
    repo.addRange(1,datetime.date(2025, 12, 15), datetime.date(2025, 12, 20))
    dates = repo.getSpaceDates(1)
    assert dates == [Availability(1, datetime.date(2025, 8, 11), 'Available', 1), Availability(9, datetime.date(2025, 12, 15), 'Available', 1), Availability(10,datetime.date(2025, 12, 16),'Available',1), Availability(11, datetime.date(2025, 12, 17),'Available', 1), Availability(12,datetime.date(2025, 12, 18), 'Available', 1), Availability(13,datetime.date(2025, 12, 19),'Available', 1), Availability(14, datetime.date(2025, 12, 20), 'Available', 1),  Availability(8, datetime.date(2026, 4, 14), 'Booked', 1)]
                                                                                                                                                                                                                    
"""
Book a date using id
"""
def test_book_date(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = AvailabilityRepository(db_connection)
    repo.book(1)
    date = repo.find(1)
    assert date == Availability(1, datetime.date(2025, 8, 11), 'Booked', 1)
                    