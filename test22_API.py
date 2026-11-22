import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# # print(response.status_code)
# # print(response.json())

data = response.json()

# # if response.status_code == 200:
# #     print("Status Check: PASS")
# # else:
# #     print("Status Check: FAIL")

# # if data["id"] == 1:
# #     print("ID Validation: PASS")
# # else:
# #     print("ID Validation: FAIL")

# # required_fields = ["userId", "id", "title", "body"]

# # for field in required_fields:
# #     if field in data:
# #         print(field, "PASS")
# #     else:
# #         print(field, "FAIL")

# response = requests.get("https://jsonplaceholder.typicode.com/invalid")

# print("Status Code:", response.status_code)
# print("Response:", response.text)

# if response.status_code == 404:
#     print("Negative Test: PASS")
# else:
#     print("Negative Test: FAIL")

# import requests
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)

#     print("Status Code:", response.status_code)
#     print("API Request Successfull")

# except requests.exceptions.RequestException as e:
#     print("API Error:", e)

import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# payload = {
#  "title": "QA Automation",
#  "body": "Learning API testing",
#  "userId":1   
# }

# response = requests.post(url, json=payload)

# print("Status Code:", response.status_code)
# print("Response", response.json())

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# payload = {
#  "title": "Updated QA Automation",
#  "body": "Learning API testing with PUT",
#  "userId":1,
#  "id":1 
# }

# response = requests.put(url, json=payload)

# print("Status Code:", response.status_code)
# print("Response", response.json())

# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"

# payload = {
#  "title": "Updated QA Automation with PATCH"
# }

# response = requests.patch(url, json=payload)

# print("Status Code:", response.status_code)
# print("Response", response.json())

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status Code:", response.status_code)
print("Response", response.json())

# if response.status_code==200:
#     print("Delete Test: PASS")
# else:
#     print("Delete Test: FAIL")


# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# data = response.json()

# JSON Validation

if isinstance(data, dict):
    print("JSON Format: PASS")
else:
    print("JSON Format: FAIL")

if data.get("id") == 1:
    print("ID Validation: PASS")
else:
    print("ID Validation: FAIL")

if data.get("userId") == 1:
    print("User ID Validation: PASS")
else:
    print("User ID Validation: FAIL")

if data.get("title"):
    print("Title Validation: PASS")
else:
    print("Title Validation: FAIL")