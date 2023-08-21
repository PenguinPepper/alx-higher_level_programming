#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    databse = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = databse.cursor()
    cmd = "SELECT cities.name FROM cities \
            INNER JOIN states on cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC"
    cur.execute(cmd, (sys.argv[4],))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
