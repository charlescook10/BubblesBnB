from lib.user import User

"""
Test that when I instantiate a user object
it gets the correct attributes
"""
def test_instantiates_correctly():
    user = User(1, "Test name", "Test username", "Test password")

    assert user.id == 1
    assert user.name == "Test name"
    assert user.username == "Test username"
    assert user.password == "Test password"

"""
When two objects with same attibutes are compared 
they are equal
"""
def test_objects_are_equal():
    user1 = User(1, "Test name", "Test username", "Test password")
    user2 = User(1, "Test name", "Test username", "Test password")

    assert user1 == user2

"""
When object is printed it appears nicely
"""
def test_prints_nicely():
    user = User(1, "Test name", "Test username", "Test password")

    assert str(user) == "User(1, Test name, Test username, Test password)"