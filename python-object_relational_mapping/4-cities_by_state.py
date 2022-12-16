#!/usr/bin/python3
# a script that lists all cities from the database hbtn_0e_4_usa
# Your script should take 3 arguments: mysql username,
# mysql password and database name
# you must use the module MySQLdb (import MySQLdb)
# Your script should connect to a
# MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by cities.id
# You can use only execute() once
# Your code should not be executed when imported
"""
    import 'MySQLdb' and 'sys' modules
"""

import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], \
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = cursor.fetchall()
    for state in states:
        print(state)
