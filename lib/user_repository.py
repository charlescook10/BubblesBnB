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
    
    # def get_username(self, user):
    #     rows = self._connection.execute(
    #         'SELECT username, password from users WHERE username = %s', [user])
    #     row = rows[0]
    #     return User(row["username"], row["password"])
    
    # def get_usernames(self):
    #     rows = self._connection.execute('SELECT username FROM users')
    #     usernames = []
    #     for row in rows:
    #         item = User(row["username"])
    #         usernames.append(item)
    #     return usernames

    # def get_username_from_id(self, id):
    #     rows = self._connection.execute('SELECT username FROM users JOIN spaces ON users.id = spaces.user_id WHERE users.id = %s', [id])
    #     row = rows[0]
    #     return User(row["username"])
    
    def add(self, user):
        rows = self._connection.execute('INSERT INTO users ( name, username, password ) VALUES (%s, %s, %s) RETURNING id', [user.name, user.username, user.password])
        user.id = rows[0]['id']
        return None

    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["name"], row["username"], row["password"])