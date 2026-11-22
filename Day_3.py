def validate_login(username, password):
    if username == "admin" and password == "admin123":
        return "True"
    else:
        return "False"

print(validate_login("admin","admin123"))
print(validate_login("admin","wrong123"))
print(validate_login("wronguser","admin123"))

def validate_login(username, password):
    if username == "admin" and password == "admin123":
        print("True")
    else:
        print("False")

validate_login("admin","admin123")

def email_validator(email):
    if "@" in email:
        return True
    else:
        return False
result = email_validator("employee@gmail.com")

print(result)


def validate_login(username, password):
    if username == "admin" and password == "admin1234":
        return True
    else:
        return False

print(validate_login("admin", "admin1234"))
print(validate_login("admin", "wrong1234"))
print(validate_login("wronguser", "admin1234"))
print(validate_login("wronguser", "wrong1234"))



check=input("Enter a password:")
def password_validator(check):
    
    if len(check)>=8:
        return "This is a valid password."
    else:
        return "This is an invalid password."

result=password_validator(check)

print(result)









def status_validator(code):
    if code == "200":
        return True
    else:
        return False

print(status_validator("200"))
print(status_validator("201"))
print(status_validator("400"))
print(status_validator("404"))
print(status_validator("500"))







test_cases = [("admin", "admin123", True), ("admin", "wrong123", False), ("wronguser", "admin123",False),  ("wronguser", "wrong123", False)]

def validate_login(username, password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

TC01=validate_login("admin", "admin123")
TC02=validate_login("admin", "wrong123")
TC03=validate_login("wronguser", "admin123")
TC04=validate_login("wronguser", "wrong123")




for test in test_cases:

    if True in test:
        print("PASSED")
    else:
        print("FAILED")











