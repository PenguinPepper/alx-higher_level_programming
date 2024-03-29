#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    databse = MySQLdb.connect(host="localhost", user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])
    cur = databse.cursor()
    word = "{}".format(sys.argv[4])
    cmd = "SELECT * FROM states WHERE name \
            LIKE BINARY %s ORDER BY states.id ASC"
    cur.execute(cmd, (word,))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    databse.close()
