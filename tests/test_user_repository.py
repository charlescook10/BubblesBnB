from lib.user import User
from lib.user_repository import UserRepository

"""
gets a list of all users 
"""
def test_gets_all_users(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql") 
    repository = UserRepository(db_connection)

    user = repository.all()

    assert user == [
        User(1, "Test_User_1", "testuser1", "abc123"),
        User(2, "Test_User_2", "testuser2", "123abc")
    ]

"""
when adding a new user it adds correctly
"""
def test_add_user(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql") 
    repository = UserRepository(db_connection)

    user = repository.add(User(3, "Test_User_3", "testuser3", "1abc23"))

    user = repository.all()

    assert user == [
        User(1, "Test_User_1", "testuser1", "abc123"),
        User(2, "Test_User_2", "testuser2", "123abc"),
        User(3, "Test_User_3", "testuser3", "1abc23")
    ] 

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_user(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, "Test_User_2", "testuser2", "123abc")