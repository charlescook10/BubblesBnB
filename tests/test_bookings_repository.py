from lib.bookings_repository import BookingRepository
from lib.availability import Availability
from lib.user import User
import datetime

def test_to_get_user_bookings(db_connection):
 db_connection.seed("seeds/bubbles_bnb.sql")
 repo = BookingRepository(db_connection)
 users_bookings = repo.find(1)
 print(users_bookings.bookings)
 assert users_bookings == User(1,'Test_User_1', 'testuser1', 'abc123', [Availability(6, datetime.date(2026, 5 , 30), 'Booked', 3)])
 
 
 