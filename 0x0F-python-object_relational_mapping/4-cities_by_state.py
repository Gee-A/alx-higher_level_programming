#!/usr/bin/python3
"""A python script that lists all cities from the database.
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
                FROM cities c INNER JOIN states s\
                ON c.state_id = s.id")
    records = cur.fetchall()
    for record in records:
        print(record)

    cur.close()
    db.close()
