#!/usr/bin/python
import MySQLdb

# DEV
# db = MySQLdb.connect(host="localhost",    # your host, usually localhost
#                     user="root",         # your username
#                     passwd="suave001",  # your password
#                     db="testdb")        # name of the data base

# LIVE
db = MySQLdb.connect(host="mysql.server295.com",    # your host, usually localhost
                     user="schedmaster",         # your username
                     passwd="poiuya123",  # your password
                     db="drlinden_sched")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("SELECT * from sched_tbl")

for row in cur.fetchall():
   print row[1]

db.close()

