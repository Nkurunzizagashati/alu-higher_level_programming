#!/usr/bin/python3
# a script that lists all states with a name
# starting with N (upper N) from the database hbtn_0e_0_usa
"""
    import 'MySQLdb' and 'sys'
"""

import sys
import MySQLdb


if __name__ == '__main__':
    data_base = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], data_base=sys.argv[3])
    a = data_base.cursor()
    a.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in a.fetchall() if state[1][0] == "N"]
