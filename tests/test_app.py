
from playwright.sync_api import Page, expect
from datetime import datetime

# -----------------------------
# Test viewing an individual space
# -----------------------------
def test_get_individual_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/spaces/1")

    # Space name
    expect(page.locator('.space-name')).to_have_text('Test_Space_1')

    # Description
    expect(page.locator('.space-description')).to_have_text("This is a description of Test_Space_1")

    # Price per night
    expect(page.locator('.space-price-per-night')).to_have_text('£10.00')

    # Host/owner name
    expect(page.locator('.user-name')).to_have_text('Test_User_1')

    # Booking button
    book_btn = page.locator('#booking-btn')
    expect(book_btn).to_have_attribute('type', 'submit')
    expect(book_btn).to_have_text('Book this space')




# -----------------------------
# Test viewing all spaces for a user
# -----------------------------
def test_get_all_spaces_for_one_user(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/user/spaces/1")

    # Update these selectors to match your current template
    expect(page.locator('h2.card-title a').nth(0)).to_have_text('Test_Space_1')
    expect(page.locator('p.card-text').nth(0)).to_have_text('This is a description of Test_Space_1')
    expect(page.locator('.text-muted').nth(0)).to_have_text('£10.00 / night')
    
    expect(page.locator('.badge').nth(0)).to_have_text('Available')  



# -----------------------------
# Test registration page loads
# -----------------------------
def test_register_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")
    page.goto(f"http://{test_web_address}/register")

    heading = page.locator("h1")
    expect(heading).to_have_text('Create your account')
    expect(page.get_by_role("button", name="Sign up")).to_be_visible()


# -----------------------------
# Test signup, login, and approval page
# -----------------------------
def test_signup_login_approval_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")

    # Register
    page.goto(f"http://{test_web_address}/register")
    page.fill("input[name='name']", "testuser5")
    page.fill("input[name='username']", "testuser5")
    page.fill("input[name='password']", "abc12345")
    page.click("button[type='submit']")

    # Login
    page.wait_for_url(f"http://{test_web_address}/signin")
    page.fill("input[name='username']", "testuser5")
    page.fill("input[name='password']", "abc12345")
    page.click("button[type='submit']")

    # Verify listings page
    page.wait_for_url(f"http://{test_web_address}/listings")
    expect(page.locator("h1")).to_have_text("All Spaces")

    # Check approval page
    page.goto(f"http://{test_web_address}/approved")
    heading = page.locator("h1")
    expect(heading).to_have_text("This booking has been approved")
    back_link = page.get_by_role("link", name="Back to listing")
    expect(back_link).to_be_visible()


# -----------------------------
# Test logout page
# -----------------------------
def test_logout_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bubbles_bnb.sql")

    # Register and login
    page.goto(f"http://{test_web_address}/register")
    page.fill("input[name='name']", "testuser6")
    page.fill("input[name='username']", "testuser6")
    page.fill("input[name='password']", "abc12345")
    page.click("button[type='submit']")

    page.goto(f"http://{test_web_address}/signin")
    page.fill("input[name='username']", "testuser6")
    page.fill("input[name='password']", "abc12345")
    page.click("button[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/listings")

    # Logout
    page.goto(f"http://{test_web_address}/logout")
    heading = page.locator("h1")
    expect(heading).to_contain_text("been logged out")
    expect(page.get_by_text("Logged out successfully!")).to_be_visible()

# -----------------------------
# Test new listing page
# -----------------------------

def test_create_new_listing(db_connection, page, test_web_address):

    db_connection.seed("seeds/bubbles_bnb.sql")


    page.goto(f"http://{test_web_address}/register")
    page.fill("input[name='name']", "testuser7")
    page.fill("input[name='username']", "testuser7")
    page.fill("input[name='password']", "abc123456")
    page.click("button[type='submit']")

    page.goto(f"http://{test_web_address}/signin")
    page.fill("input[name='username']", "testuser7")
    page.fill("input[name='password']", "abc123456")
    page.click("button[type='submit']")
    page.wait_for_url(f"http://{test_web_address}/listings")

    page.goto(f"http://{test_web_address}/new_listing")
    expect(page.locator("h1")).to_have_text("List a new space")

    page.fill("input[name='name']", "My Test Space")
    page.fill("textarea[name='description']", "A description of my test space")
    page.fill("input[name='price_per_night']", "25.00")
    page.fill("input[name='available_from']", "2025-12-01")
    page.fill("input[name='available_to']", "2025-12-10")

    page.click("button[type='submit']")


    page.wait_for_url(f"http://{test_web_address}/user/spaces/3", timeout=10000)

    space_card = page.locator("div.card", has_text="My Test Space")
    expect(space_card).to_be_visible()

    description = space_card.locator("p.card-text")
    expect(description).to_have_text("A description of my test space")

    price = space_card.locator("p.text-muted")
    expect(price).to_have_text("£25.00 / night")

    back_link = page.get_by_role("link", name="Back to all listings")
    expect(back_link).to_be_visible()

