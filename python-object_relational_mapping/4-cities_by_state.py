#!/usr/bin/python3
"""
    this script will list all cities
    from our database Your script should take
    3 arguments: mysql username, mysql password
    and database name

    You must use the module MySQLdb (import MySQLdb)

    Your script should connect to a MySQL server
    running on localhost at port 3306

    Results must be sorted in ascending
    order by cities.id

    You can use only execute() once

    Results must be displayed as they
    are in the example below

    Your code should not be executed when imported
"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )
    cursor = db.cursor()

    command = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    cursor.execute(command)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
