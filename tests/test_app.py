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
    div_tags = page.locator('div')
    expect(div_tags).to_have_text(['Test_Space_1\nThis is a description of Test_Space_1\n10.0\nTest_User_1'])