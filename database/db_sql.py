from database.queries import CREATE_TASK_TABLE, INSERT_TASK, SELECT_ALL_TASK
import datetime
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(os.environ["DB_URL"])
if conn!=None:
    print("\nDB Connected Successfully!")

def createTable():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(CREATE_TASK_TABLE)

def putOne(name, date, status):
    with conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(INSERT_TASK, (name, date, status))
                print("\nData inserted Successfully!\n")
            except:
                print("\nEnter valid date!\n")

def getAll():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_ALL_TASK)
            return cursor.fetchall()

def getFuture():
    pass

def getOver():
    pass
