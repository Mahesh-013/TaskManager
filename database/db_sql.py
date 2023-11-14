import os
import psycopg2


from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(os.environ["DB_URL"])
if conn!=None:
    print("DB Connected Successfully!")

def putOne(date, name, status):
    pass

def getAll():
    pass

def getFuture():
    pass

def getOver():
    pass
