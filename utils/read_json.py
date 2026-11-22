import json

with open("test_data.json", "r") as file:
    data=json.load(file)

print(data)

for user in data["users"]:
    print(user["test_case"], "->", user["expected_status"])