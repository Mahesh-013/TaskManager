from database.queries import CREATE_TASK_TABLE, INSERT_TASK
from database.queries import SELECT_ALL_TASKS, SELECT_COMPLETED, SELECT_IN_PROGRESS, SELECT_FUTURE_TASKS, SELECT_SORTED, SELECT_DEADLINE_TASK, SELECT_BY_DATE
import datetime
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(os.environ["DB_URL"])
if conn!=None:
    print("\nDB Connected Successfully!")

today=datetime.date.today()

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
            cursor.execute(SELECT_ALL_TASKS)
            return cursor.fetchall()

def getOver():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_COMPLETED)
            return cursor.fetchall()

def getInProgress():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_IN_PROGRESS)
            return cursor.fetchall()

def getFuture():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_FUTURE_TASKS)
            return cursor.fetchall()

def getSorted():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_SORTED)
            return cursor.fetchall()

def getDeadlineExceed():
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_DEADLINE_TASK, (today, ))
            return (cursor.fetchall(), today)

def getByDate(date):
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(SELECT_BY_DATE, (today, date))
            return cursor.fetchall()