import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shalini26&",
    database="Employees"
)

print("Database connected successfully")

cursor = connection.cursor()
cursor.execute("SELECT * FROM users WHERE id = 6")

result = cursor.fetchone()

print("Actual name:", result[1])


expected_name = "Sahil"
print("Expected name:", expected_name)
if result[1] == expected_name:
    print("PASSED")
else:
    print("FAILED")


cursor.execute("SELECT * FROM users WHERE id = 6")
check = cursor.fetchone()
print(check)