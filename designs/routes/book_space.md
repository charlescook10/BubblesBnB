
# Spaces Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Book a space route
PUT /book-space/<id>
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

# PUT /book-space/<id>
#  Expected response (200 OK):
"""
conn = get_flask_database_connection(app)
repo = SpacesRepository(db_conn)

space = repo.find(id)

spaces = repo.update()
return render_template('artists/index.html', spaces=spaces)
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /spaces
  Expected response (200 OK):
"""
def test_get_spaces(web_client):
  db_connection.seed('seeds/bubbles_bnb.sql')

  page.goto(f"http://{test_web_address}/spaces")

  spaces = page.locator('.spaces_listing')
  expect(spaces).to_have_text([
    'Test_Space_1', 'This is a description of Test_Space_1', '10.00'
  ])

```

