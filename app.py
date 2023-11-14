from database.db_sql import createTable, putOne, getAll, getFuture, getOver

print("App started!")
choice="""

1) Enter a new Note
2) View all tasks
3) View future tasks
4) View completed
5) View tasks in progress
6) View Formatted task
7) Delete a task
8) Clean List
q) Exit

"""

createTable()

def addNew():
    
    name=input("Enter the task: ")
    date=input("Enter date to finish task YYYY-MM-DD: ")
    status=input("Enter the statusof task 0(Completed) / 1(In Progress) / 2(Yet to): ")

    if name and date and status in ('0','1','2'):
        putOne(name, date, status)
    else:
        print("\nEnter Valid Status!\n")
        addNew()
        return

def viewAll():
    tasks=getAll()
    print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
    for task in tasks:
        status=task[3]
        status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
        print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)

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