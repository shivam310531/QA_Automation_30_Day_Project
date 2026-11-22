import os 
from dotenv import load_dotenv

load_dotenv()

import requests
import pytest

# @pytest.fixture
# def api_url():
#     return "https://jsonplaceholder.typicode.com/posts/1"

# def test_get_post(api_url):
#     response = requests.get(api_url)

#     assert response.status_code==200

#     data= response.json()

#     assert data["id"] == 1
#     assert data["userId"] == 1
#     assert data["title"] != ""
#     assert data["body"] != ""

# @pytest.mark.parameterize("post_id",[1,2,3])
# def test_multiple_posts(post_id):
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

#     response-requests.get(url)

#     assert response.status_code==200

#     data=response.json()

#     assert data["id"] ==post_id
import requests
import mysql.connector
import uuid

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title":"QA Automation",
        "body":"Testing POST API",
        "userId":1
    }
    response = requests.post(url,json=payload)
    assert response.status_code ==201
    data= response.json()
    assert data["title"]=="QA Automation"
    assert data["userId"]==1

def test_api_to_database_validation():

    # Step 1: Unique test data
    email = f"qa_{uuid.uuid4().hex[:8]}@test.com"

    payload = {
        "name": "Automation Tester",
        "email": email
    }

    # Step 2: Perform API action
    response = requests.post(
        "http://127.0.0.1:5000/users",
        json=payload
    )

    # Step 3: Validate API response
    assert response.status_code == 201

    api_data = response.json()
    user_id = api_data["id"]

    # Step 4: Connect to MySQL
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="qa_day23"
    )

    cursor = connection.cursor()

    # Step 5: Fetch the same user from DB
    cursor.execute(
        "SELECT name, email FROM users WHERE id = %s",
        (user_id,)
    )

    db_data = cursor.fetchone()

    # Step 6: Compare API and DB data
    assert db_data is not None
    assert db_data[0] == api_data["name"]
    assert db_data[1] == api_data["email"]

    cursor.close()
    connection.close()