#!/usr/bin/python3
"""script lists all staes with a name starting with 'N' from the database.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name\
                LIKE 'N%' ORDER BY states.id ASC")
    records = cur.fetchall()
    for record in records:
        print(record)

    cur.close()
    db.close()
