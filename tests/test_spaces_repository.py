from lib.spaces_repository import SpaceRepository
from lib.spaces import Space

def test_all(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = SpaceRepository(db_connection)
    assert repo.all() == [
                Space(1, 'Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 'img/mock-1.jpg', 1),
                Space(2, 'Test_Space_2', 'This is a description of Test_Space_2', 10.0, False, 'img/mock-2.jpg', 1),
                Space(3, 'Test_Space_3', 'This is a description of Test_Space_3', 10.0, False, 'img/mock-3.jpg', 2),
                Space(4, 'Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 'img/mock-4.jpg', 2)
    ]


def test_get_single_space(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = SpaceRepository(db_connection)
    space = repo.find(4)
    assert space == Space(4, 'Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 'img/mock-4.jpg', 2)

def test_update_a_record(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = SpaceRepository(db_connection)

    space = repo.find(4)
    assert space == Space(4, 'Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 'img/mock-4.jpg', 2)

    new_space = Space(4, 'Test_Space_New_Name', 'This is a description of Test_Space_1', 10.0, False, 'img/mock-4.jpg', 2)

    updated_space = repo.update(new_space)

    assert updated_space ==  Space(4, 'Test_Space_New_Name', 'This is a description of Test_Space_1', 10.0, False, 'img/mock-4.jpg', 2)
    
    
    def test_add_new_listing(db_connection):
        db_connection.seed("seeds/bubbles_bnb.sql")
        repo = SpaceRepository(db_connection)
        result = repo.add_new_listing()
        assert result == [
                Space('Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 'img/mock-1.jpg', 1),
                Space('Test_Space_2', 'This is a description of Test_Space_2', 10.0, False, 'img/mock-2.jpg', 1),
                Space('Test_Space_3', 'This is a description of Test_Space_3', 10.0, False, 'img/mock-3.jpg', 2),
                Space('Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 'img/mock-4.jpg', 2),
                Space('Test_Space_5', 'This is a description of Test_Space_5', 10.0, False, 'img/mock-5.jpg', 2)

    ]
        
        
    def test_delete_space(db_connection):
        db_connection.seed("seeds/bubbles_bnb.sql")
        repository = SpaceRepository(db_connection)
        repository.delete(3) 
        result = repository.all()
        assert result == [
                Space(1, 'Test_Space_1', 'This is a description of Test_Space_1', 10.0, False,'img/mock-1.jpg', 1),
                Space(2, 'Test_Space_2', 'This is a description of Test_Space_2', 10.0, False,'img/mock-2.jpg', 1),
                Space(4, 'Test_Space_4', 'This is a description of Test_Space_4', 10.0, False,'img/mock-4.jpg', 2)
            ]    

def test_gets_all_spaces_from_user_id(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = SpaceRepository(db_connection)

    spaces_list = repo.find_by_user(1)

    assert spaces_list == [
        Space(1, "Test_Space_1", "This is a description of Test_Space_1", 10.0, False,'img/mock-1.jpg', 1),
        Space(2, "Test_Space_2", "This is a description of Test_Space_2", 10.0, False,'img/mock-2.jpg', 1)
    ]