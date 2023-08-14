#!/usr/bin/python3
"""
script that lists all cities from the database
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    databse = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = databse.cursor()
    cmd = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    cur.execute(cmd)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
