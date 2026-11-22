import mysql.connector 

def create_connection():

    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shalini26&",
    database="Employees"
)



def validate_user_name(user_id, expected_name):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.close()
    connection.close()

    cursor.execute("SELECT * FROM users WHERE id =%s", (user_id,))

    result = cursor.fetchone()
    print("Expected:", expected_name)
    print("Actual:", result[1])

    if expected_name == result[1]:
        print("PASSED") 
    else:
        print("FAILED")



validate_user_name(2,"Shashi")

