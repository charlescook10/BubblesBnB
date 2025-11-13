from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(db_connection, page, test_web_address):
#     # We seed
#     db_connection.seed("seeds/bubbles_bnb.sql")
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

def test_get_individual_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces/1")
    
    
    expect(page.locator('.space-name')).to_have_text('Test_Space_1')
    expect(page.locator('.space-description')).to_have_text('This is a description of Test_Space_1')
    expect(page.locator('.space-price-per-night')).to_have_text('10.0')
    expect(page.locator('.user-name')).to_have_text('Test_User_1')

    book_btn = page.locator('#booking-btn')

    expect(book_btn).to_have_attribute('type', 'submit')
    expect(book_btn).to_have_text('Book Here')
    

"""
GET /spaces/user_id_1
When we call a user_id we get a list of spaces 
for that specific user
"""
def test_get__all_spaces_for_one_user(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/user/spaces/1")

    expect(page.locator('.space-name').nth(0)).to_have_text('Test_Space_1')
    expect(page.locator('.space-description').nth(0)).to_have_text('This is a description of Test_Space_1')

    
"""
GET /approved
returns the correctly formatted webpage
"""
def test_approval_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/approved")
    heading = page.locator("h1")
    expect(heading).to_have_text('This booking has been approved')
    expect(page.get_by_text("Back to all listings")).to_be_visible();
    expect(page.get_by_role("link", name="Back to all listings"))


"""
GET /register
returns the correctly formatted webpage
"""

def test_register_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/register")
    heading = page.locator("h1")
    expect(heading).to_have_text('Create your account')
    expect(page.get_by_text('Sign up')).to_be_visible()
    
"""
GET /register
returns the correctly formatted webpage
"""

def test_login_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/login")
    heading = page.locator("h1")
    expect(heading).to_have_text('Log in to your account')
    expect(page.get_by_text('Login')).to_be_visible()
    
