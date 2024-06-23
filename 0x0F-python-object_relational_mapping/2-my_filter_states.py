#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Getting command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connecting to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )

        # Creating a cursor object to interact with the database
        cursor = db.cursor()

        # Creating the SQL query with the user input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Executing the SQL query
        cursor.execute(query, (state_name,))

        # Fetching all the rows from the executed query
        states = cursor.fetchall()

        # Displaying the results
        for state in states:
            print(state)

        # Closing the cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")

