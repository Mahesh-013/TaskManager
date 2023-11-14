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
    putOne()

def viewAll():
    data=getAll()

def viewFuture():
    data=getAll_Future()

def viewCompleted():
    data=getAll_Over()

while ip:=input()!='q':
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