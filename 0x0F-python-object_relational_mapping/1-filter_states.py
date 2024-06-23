"""
This script lists all ststes with a 'name' starting
with letter 'N' from the database
"""

import MySQL
from sys import argv

if __name__ == '__main__':
    """ Access to the database and get the ststes
    from the database.
    """
    db = MySQL.connect(host="localhost", user = argv[1], port = 3306,
            passwd = argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
