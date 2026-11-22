name = "Shivam Sharma"
role = "Automation Tester"
print("Name:", name)
print("Role:", role)
print("I am starting Python for automation testing!")

name = "Shivam Sharma"
age = 27
experience = 3.5
is_automation_tester = True

print(name)
print(age)
print(experience)
print(type(is_automation_tester))

browser = input("Enter a browser name: ")
print("Hi, I am using the", browser,"browser")

if browser =="Chrome" or "Edge":
    print("Great! this browser is supported.")
else:
    print("Iam so sorry, this browser is not supported.")

browsers = ["Chrome", "Edge", "Firefox"]
print(browsers)
print(browsers[0])
print(browsers[1])

browsers = ["Chrome", "Edge", "Firefox"]
for browser in browsers:
    print("Testing:", browser)

for browser in browsers:
    if browser =="Chrome" or browser == "Edge":
        print(browser, "is supported")
    else:
        print(browser, "is not supported")

test_cases = ["Login", "Search", "Checkout", "Logout"]
for test in test_cases:
        print("Executing test:", test )

test_cases = ["Login", "Search", "Checkout", "Logout"]
for test in test_cases:
     if test == "Login" or test == "Logout":
        print("Test Result: PASS")
     else:
        print("Test Result: FAIL")

test_case = "Login"
expected_result = input("Enter the expected result here: ")
actual_result = input("Enter the actual result here: ")

if actual_result == expected_result:
    print("This test case is PASSED")

else:
    print("This test case is FAILED")

test_cases = [("Login", "PASS", "PASS"), ("Search", "PASS", "PASS"), ("Checkout", "PASS", "FAIL"), ("Logout", "PASS", "FAIL")]
for (test, expected, actual) in test_cases:
    print("Test:", test)
    if expected == actual:
        print("PASS")

    else:
        print("FAIL")

def greet():
    print("Hi, Iam learning Automation")

greet()

def check_test(test, expected, actual):
    if expected == actual:
            print("PASS")
    
    else:
            print("FAIL")
check_test("Login", "PASS", "FAIL")
check_test("Search", "PASS", "PASS")
check_test("Checkout", "PASS", "PASS")
check_test("Logout", "PASS", "PASS")

def check_test(test_name, expected, actual):
     if actual == expected:
          return "PASS"
     else:
          return "FAIL"

result = check_test("Login", "PASS", "FAIL")
print("Login result:", result) 

def test_case(username, password):
     if username == "Shivam" and password == 1234:
          return "PASS"

     else:
          return "FAIL"

result = test_case("Shalini", 1234)
print("The result of this login test is:", result)


test_case = {"name":"Login Test", "expected":"PASS", "actual":"PASS"}
print(test_case)
print(test_case["name"])
print(test_case["expected"])
print(test_case["actual"])

test_case = {"name":"Login Test:", "expected":"PASS", "actual":"FAIL"}

if test_case["actual"] == test_case["expected"]:
     print(test_case["name"], "PASS")

else:
     print(test_case["name"], "FAIL") 

test_cases = [{"name":"Login Test:", "expected":"PASS", "actual":"PASS"}, {"name":"Search Test:", "expected":"PASS", "actual":"PASS"}, {"name":"Checkout Test:", "expected":"PASS", "actual":"PASS"}, {"name":"Logout Test:", "expected":"PASS", "actual":"PASS"}]
for test in test_cases:
    if test_case["actual"] == test_case["expected"]:
        print(test["name"], "PASS")

    else:
        print(test["name"], "FAIL") 



















        