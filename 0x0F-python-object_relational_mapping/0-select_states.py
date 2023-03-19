#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    databse = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = databse.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
