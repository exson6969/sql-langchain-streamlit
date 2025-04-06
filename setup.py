import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

SQL_HOST=os.getenv("SQL_HOST")
SQL_USER=os.getenv("SQL_USER")
SQL_PASSWORD=os.getenv("SQL_PASSWORD")

# Database connection details
db_config = {
    "host": SQL_HOST,
    "user": SQL_USER,
    "password": SQL_PASSWORD,  # Ask users to enter if needed
}

# Read SQL script from file
with open("setup.sql", "r") as file:
    setup_sql = file.read()

try:
    # Connect to MySQL server
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Split SQL commands and execute each one
    for statement in setup_sql.split(";"):
        if statement.strip():
            cursor.execute(statement)

    conn.commit()
    print("Database setup complete!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
