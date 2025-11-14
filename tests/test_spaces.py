from lib.spaces import Space

def test_correct_construction():
    spaces = Space(
        1, 
        'Test_Space_1', 
        'This is a description of Test_Space_1', 
        10.0, 
        False, 
        'img/mock-1.jpg',  
        1
    )
    assert spaces.id == 1
    assert spaces.name == 'Test_Space_1'
    assert spaces.description == 'This is a description of Test_Space_1'
    assert spaces.price_per_night == 10.0
    assert spaces.booked_flag == False
    assert spaces.image_path == 'img/mock-1.jpg'
    assert spaces.user_id == 1

def test_comparison():
    space_1 = Space(
        1, 
        'Test_Space_1', 
        'This is a description of Test_Space_1', 
        10.0, 
        False, 
        'img/mock-1.jpg',  
        1
    )
    space_2 = Space(
        1, 
        'Test_Space_1', 
        'This is a description of Test_Space_1', 
        10.0, 
        False, 
        'img/mock-1.jpg',  
        1
    )
    assert space_1 == space_2
