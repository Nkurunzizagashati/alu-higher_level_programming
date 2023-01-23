#!/usr/bin/python3
'''
    this script takes in the name of
    a state as an argument and lists all
    cities of that state, using the database
    hbtn_0e_4_usa
    Your script should take
    4 arguments: mysql username,
    mysql password, database name and state
    name (SQL injection free!)

    You must use the module
    MySQLdb (import MySQLdb)

    Your script should connect to a MySQL server
    running on localhost at port 3306

    Results must be sorted in
    ascending order by cities.id

    You can use only execute() once

    The results must be displayed as they are in
    the example below

    Your code should not be executed when imported
'''


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        port=3306
    )

    state_name = sys.argv[4]

    cursor = db.cursor()

    command = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""

    cursor.execute(command, (state_name,))

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
