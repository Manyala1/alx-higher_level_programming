#!/usr/bin/python3
import sys
import MySQLdb

if __name++ == "__main__":
    #Getting command line argumrnts
    mysql_username = sys.argv[1]
    mysq_password = sys_argv[2]
    db_name = sys.argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = mysql_username,
            db = db_name
        )
    
    #Creating a cursor object to interact with the database
    cursor = db.cursor()

    #creating the SQL querru to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #fetching all the rows from the executed query
    states = cursor.fetchall()

    # Displaying the results
    for state in states:
        print(state)

    # closing the cursor and database connection
    cursor.close()
    db.clos()
