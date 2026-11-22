import os 
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password= os.getenv("DB_PASSWORD"),
        database="qa_day23"
    )


@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))

    connection.commit()

    user_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return jsonify({
        "message": "User created successfully",
        "id": user_id,
        "name": name,
        "email": email
    }), 201


if __name__ == "__main__":
    app.run(debug=True)



