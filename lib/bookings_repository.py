from lib.availability import Availability
from lib.user import User

class BookingRepository:
 def __init__(self, connection):
  self._connection = connection
 def find(self, user_id):
  rows = self._connection.execute('SELECT users.id, users.name, users.username, users.password, a.id AS a_id, a.date, a.status, a.space_id FROM users JOIN bookings ON users.id=bookings.user_id JOIN availabilities a ON a.id= bookings.availability_id WHERE users.id= %s' , [user_id])
  row = rows[0]
  availabilities = [Availability(row_a['a_id'], row_a['date'], row_a['status'], row_a['space_id']) for row_a in rows]
  return User(row['id'], row['name'], row['username'], row['password'], availabilities)