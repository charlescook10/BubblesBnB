#Instantiate
class User():
    def __init__ (self, id, name, username, password, bookings=None):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.bookings = bookings or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.username}, {self.password})"