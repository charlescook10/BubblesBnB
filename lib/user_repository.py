from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')

        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["username"], row["password"])
            users.append(item)
        return users
    
    def add(self, user):
        rows = self._connection.execute('INSERT INTO users ( name, username, password ) VALUES (%s, %s, %s) RETURNING id', [user.name, user.username, user.password])
        user.id = rows[0]['id']
        return None

    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["name"], row["username"], row["password"])