import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def select_all_task(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM DATA")

    rows = cur.fetchall()

    for row in rows:
        print(row[0])

def insertData(conn,data):
    sql = ''' INSERT INTO DATA(Temperature,Humidity,Soil)
                  VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid
