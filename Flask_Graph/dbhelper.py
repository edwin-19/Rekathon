import sqlite3 as sql
import sys
from sqlite3 import *

db = "database/myDB.db"

def openDB():
    try:
        conn = sql.connect(db)
    except:
        print("Error open db.\n")
        return False

    curr = conn.cursor()
    return [conn, curr]

def createTable():
    openDB()
    conn = sql.connect(db)

    if not checkTableExists(conn, tablename="MYDATA"):
        conn.execute(" CREATE TABLE MYDATA( ID INTEGER PRIMARY KEY AUTOINCREMENT, HUMIDITY INTEGER NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50),SALARY REAL); ")
        conn.commit()
    else:
        print("TABLE EXISTS")

def checkTableExists(dbconn, tablename):
    dbcur = dbconn.cursor()
    dbcur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False