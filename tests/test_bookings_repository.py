from lib.bookings_repository import BookingRepository
from lib.availability import Availability
from lib.user import User
import datetime

def test_to_get_user_bookings(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = BookingRepository(db_connection)
    users_bookings = repo.find(1)
    assert users_bookings == User(1,'Test_User_1', 'testuser1', 'abc123', [Availability(6, datetime.date(2026, 5 , 30), 'Booked', 3)])
    
def test_create_booking(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = BookingRepository(db_connection)
    repo.create(1,8)
    users_bookings = repo.find(1)
    assert users_bookings == User(1,'Test_User_1', 'testuser1', 'abc123', [Availability(6, datetime.date(2026, 5 , 30), 'Booked', 3), Availability(8, datetime.date(2026, 4, 14), 'Booked', 1)])
