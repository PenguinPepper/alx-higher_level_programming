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
    sqcmd = "SELECT * FROM states WHERE CAST(name AS BINARY)  RLIKE BINARY 'N' ORDER BY states.id ASC"
    cur.execute(sqcmd)
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
