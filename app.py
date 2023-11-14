from database.db_sql import putOne, getAll, getFuture, getOver

print("App started!")
choice="""
1) Enter a new Note
2) View all tasks
3) View future tasks
4) View completed
q) Exit
"""

def addNew():
    date=input("Enter date in YYYY-MM-DD: ")
    name=input("Enter the task: ")
    status=input("Enter the statusof task 0/1: ")

    putOne(date, name, status)

def viewAll():
    data=getAll()

def viewFuture():
    data=getFuture()

def viewCompleted():
    data=getOver()

while (ip:=input(choice))!='q':
    if ip=='1':
        addNew()

    elif ip=='2':
        viewAll()

    elif ip=='3':
        viewFuture()

    elif ip=='4':
        viewCompleted()

    else:
        print("Quiting!")
        break