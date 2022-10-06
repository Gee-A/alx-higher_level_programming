#!/usr/bin/python3
"""A python script that takes in arguments and displays all values in the
states table of a database where name matches the argument and most be
save from MySQL injection.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s\
                ORDER BY states.id ASC", (sys.argv[4],))
    records = cur.fetchall()
    for record in records:
        print(record)
