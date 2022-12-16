#!/usr/bin/python3
# a script that lists all states from the database hbtn_0e_0_usa
"""
    importing 'MySQLdb' and 'sys'
    modules
"""

import sys
import MySQLdb


if __name__ == "__main__":
    data_base = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], data_base=sys.argv[3])
    a = data_base.cursor()
    a.execute("SELECT * FROM 'states' WHERE BINARY 'name' == '{}'".format(sys.argv[4]))
    [print(state) for state in a.fetchall()]
