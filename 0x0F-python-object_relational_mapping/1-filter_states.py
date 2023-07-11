#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    databse = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = databse.cursor()
    variable = 'N'
    sqcmd = f"SELECT * FROM states WHERE name LIKE '{variable}%' ORDER BY states.id ASC"
    cur.execute(sqcmd)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
