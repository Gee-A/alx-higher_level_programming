#!/usr/bin/python3

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT c.name\
                FROM cities c INNER JOIN states s\
                ON c.state_id = s.id\
                WHERE s.name = %s\
                ORDER BY c.id ASC", (sys.argv[4],))
    records = cur.fetchall()
    print(", ".join([record[0] for record in records]))

    cur.close()
    db.close()
