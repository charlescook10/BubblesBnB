from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
GET /spaces
  Expected response (200 OK):
"""
def test_get_spaces(db_connection, page, test_web_address):
  db_connection.seed('seeds/bubbles_bnb.sql')

  page.goto(f"http://{test_web_address}/spaces")

  spaces = page.locator('.spaces_listing')
  expect(spaces).to_have_text([
    'Test_Space_1', 'This is a description of Test_Space_1',
    'Test_Space_2', 'This is a description of Test_Space_2',
    'Test_Space_3', 'This is a description of Test_Space_3',
    'Test_Space_4', 'This is a description of Test_Space_4' 
    ])
