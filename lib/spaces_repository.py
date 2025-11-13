from lib.spaces import Space
from lib.user import User

class SpaceRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price_per_night"], row["booked_flag"], row["user_id"])
            spaces.append(item)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["booked_flag"], row["user_id"])
    
    def update(self, space):
        rows = self._connection.execute('UPDATE spaces SET name=%s, description=%s, price_per_night=%s, booked_flag=%s, user_id=%s WHERE id = %s RETURNING *', [space.name, space.description, space.price_per_night, space.booked_flag, space.user_id, space.id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["booked_flag"], row["user_id"])
    
    
    def add_new_listing(self, space):
        rows = self._connection.execute(
            """
            INSERT INTO spaces (name, description, price_per_night, booked_flag, user_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, name, description, price_per_night, booked_flag, user_id;
            """,
            [space.name, space.description, space.price_per_night, space.booked_flag, space.user_id]
        )

        row = rows[0]
        return Space(
            row["id"],
            row["name"],
            row["description"],
            row["price_per_night"],
            row["booked_flag"],
            row["user_id"]
        )

    
    
    def delete_space(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None
    
    def find_by_user(self, user_id):
        rows = self._connection.execute('SELECT * from spaces WHERE user_id = %s', [user_id])
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price_per_night"], row["booked_flag"], row["user_id"])
            spaces.append(item)
        return spaces
    