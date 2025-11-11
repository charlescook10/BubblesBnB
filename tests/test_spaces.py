from lib.spaces import Spaces

def test_correct_construction():
    spaces = Spaces(1, 'Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 1)
    assert spaces.id == 1
    assert spaces.name == 'Test_Space_1'
    assert spaces.description == 'This is a description of Test_Space_1'
    assert spaces.price_per_night == 10.0
    assert spaces.booked_flag == False
    assert spaces.user_id == 1

