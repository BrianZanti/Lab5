__author__ = 'khn9mc'

import operator
import sys
import csv
import sqlite3

database = 'coursedata.db'  # global variable to hold database name

def write_to_db(deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor):
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "insert into coursedata values(?,?,?,?,?,?,?)"
        cur.execute(sql_cmd,(deptID, courseNum, semester, meetingType, seatsTaken, seatsOffered, instructor) )
#comment - trm2yf
def find_course():
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "SELECT * FROM coursedata WHERE deptID = 'CS'"
        cur.execute(sql_cmd)
        for thing in cur.fetchall():
            print thing

with open('test.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        write_to_db(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

find_course()
dictA = {}
conn = sqlite3.connect(database)
with conn:
    cur = conn.cursor()
    sql_cmd = "SELECT * FROM coursedata"
    cur.execute(sql_cmd)
    for thing in cur.fetchall():
        if thing[6] in dictA:
            dictA[thing[6]] = dictA[thing[6]] + thing[4]
        else:
            dictA[thing[6]] = thing[4]
print dictA

dictB = {}
conn = sqlite3.connect(database)
with conn:
    cur = conn.cursor()
    sql_cmd = "SELECT * FROM coursedata WHERE deptID = 'CS'"
    cur.execute(sql_cmd)
    for thing in cur.fetchall():
        if thing[1] in dictB:
            dictB[thing[1]] = dictB[thing[1]] + thing[4]
        else:
            dictB[thing[1]] = thing[4]

print dictB

print "this lab is so not monkey!!!!"


print "stuff"

