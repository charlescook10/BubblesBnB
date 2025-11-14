from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
GET /spaces
  Expected response (200 OK):
"""
def test_get_spaces(db_connection, page, test_web_address):
  db_connection.seed('seeds/bubbles_bnb.sql')

  page.goto(f"http://{test_web_address}/register")
  page.fill("input[name='name']", "testuser4")
  page.fill("input[name='username']", "testuser4")
  page.fill("input[name='password']", "abc12345")  
  page.click("button[type='submit']")

  page.wait_for_url(f"http://{test_web_address}/signin", timeout=10000)
  page.fill("input[name='username']", "testuser4")
  page.fill("input[name='password']", "abc12345")
  page.click("button[type='submit']")

  page.wait_for_url(f"http://{test_web_address}/listings", timeout=10000)
  page.wait_for_selector("h1:has-text('All Spaces')", timeout=10000)

  space_names = page.locator(".card-title a")
  space_descriptions = page.locator(".card-text")

  expect(space_names).to_have_text([
    'Test_Space_1',
    'Test_Space_2',
    'Test_Space_3',
    'Test_Space_4'
    ])
  
  expect(space_descriptions).to_have_text([
    'This is a description of Test_Space_1',
    'This is a description of Test_Space_2',
    'This is a description of Test_Space_3',
    'This is a description of Test_Space_4' 
    ])
  
  def test_post_spaces():
    pass