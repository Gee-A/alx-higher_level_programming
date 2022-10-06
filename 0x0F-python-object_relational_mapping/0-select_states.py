#!/usr/bin/python3
"""Connects to a database and execute a query using a python script.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    records = cur.fetchall()
    for record in records:
        print(record)

    cur.close()
    db.close()
