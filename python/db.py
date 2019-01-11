#!/usr/bin/python
"""This python scripts is designed for db common task which should be done quickly
	sudo pip install MySQL-python

"""

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="atwork")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("SHOW columns FROM aw_user")
print [column[0] for column in cur.fetchall()]

# Use all the SQL you like
cur.execute("SELECT * FROM aw_user")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
