browser = "Chrome"
print(browser)
print(browser.lower())
print(browser.upper())
print(browser.strip())

message = "Login successful"
print("successful" in message)
print ("failed" in message)

url = "https://example.com/login"

print(url)
print(url.replace("login","logout"))

status = " Login Successful "

status = status.strip()

print(status)

print("Login" in status)
print(status.lower())

test_case = ["Login", "Search", "Checkout", "Logout"]

print(test_case)

test_case.append("Logout")
print(test_case)

print(test_case)

test_case.remove("Checkout")

print(test_case)
print(len(test_case))

print(test_case)

test_case.append("Checkout")

print(test_case)

test_case = ["Login", "Search", "Checkout", "Logout"]
print("The number of test are:", len(test_case))
for test in test_case:
    print("Test:", test)


test_case = ["Login", "Search", "Checkout", "Logout"]
test_case[2] = "Profile"

print(test_case)

check = input("Search for a test case: ")
test_case = ["Login", "Search", "Checkout", "Logout"]
if check in test_case:
    print(check, "test is available in the test case.")
else:
    print(check, "test is not available in the test case.")

test_case ={"name":"Login", "status":"PASS"}

print(test_case)

test_cases = [{"id":"TC01", "status":"PASS"}, {"id":"TC02", "status":"FAIL"}, {"id":"TC03", "status":"PASS"}, {"id":"TC04", "status":"FAIL"}]
for test in test_cases:
    if test["status"] == "PASS":
        print(test, "is passed")
for test in test_cases:
    print(test["id"]), test["status"]


def validate_login(username, password):
    if username != "" and password == "12345":
        return "PASS"
    else:
        return "FAIL"

print(validate_login("Shivam", "2345"))