#!/usr/bin/env python
"""A python script that interact with a database.
"""

import MySQLdb
import sys

db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3], charset='utf8')

string = "SELECT * FROM states WHERE states.name = '{}'\
         ORDER BY states.id ASC".format(sys.argv[4])
cur = db.cursor()
cur.execute(string)
records = cur.fetchall()
for record in records:
    print(record)
