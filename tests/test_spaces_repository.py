from lib.spaces_repository import SpaceRepository
from lib.spaces import Space

def test_all(db_connection):
    db_connection.seed("seeds/bubbles_bnb.sql")
    repo = SpaceRepository(db_connection)
    assert repo.all() == [Space(1, 'Test_Space_1', 'This is a description of Test_Space_1', 10.0, False, 1),
                          Space(2, 'Test_Space_2', 'This is a description of Test_Space_2', 10.0, False, 1),
                          Space(3, 'Test_Space_3', 'This is a description of Test_Space_3', 10.0, False, 2),
                          Space(4, 'Test_Space_4', 'This is a description of Test_Space_4', 10.0, False, 2)
                          ]


def test_find():
    pass