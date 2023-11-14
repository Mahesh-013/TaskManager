from database.db_sql import createTable, putOne, getAll, getOver, getInProgress, getFuture, getSorted, getDeadlineExceed

createTable()

def addNew():
    name=input("Enter the task: ")
    date=input("Enter deadline for task YYYY-MM-DD: ")
    status=input("Enter the status of task 0(Completed) / 1(In Progress) / 2(Yet to): ")

    if name and date and status in ('0','1','2'):
        putOne(name, date, status)
    else:
        print("\nEnter Valid Status!\n")
        addNew()
        return

def viewAll():
    tasks=getAll()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere is no task currently in the DB!\n")

def viewCompleted():
    tasks=getOver()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_COMPLETED", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is no completed task currently!\n")

def viewInProgress():
    tasks=getInProgress()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_IN_PROGRESS", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is no task in progress currently!\n")

def viewFuture():
    tasks=getFuture()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_YET_TO", "TASK_DEADLINE\n", sep="\t\t\t")
        for task in tasks:
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ")
    else:
        print("\nThere is future assigned task currently!\n")

def viewSorted():
    tasks=getSorted()
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="Completed" if status==0 else("In Progress" if status==1 else "Yet to")
            print("  ", task[0], "\t\t ", task[1], "\t\t", task[2],"\t\t\t  ",  status)
    else:
        print("\nThere is no task currently in the DB!\n")

def viewDeadBeyond():
    tasks, today=getDeadlineExceed()
    # today=datetime
    if len(tasks)!=0:
        print("\nTASK_ID", "TASK_LIST", "TASK_DEADLINE", "TASK_OVERRUN_BY (in days)", "TASK_STATUS\n", sep="\t\t\t")
        for task in tasks:
            status=task[3]
            status="In Progress" if status==1 else "Yet to"
            print("  ", task[0], "\t\t ", task[1], "\t\t\t", task[2],"\t\t\t  ", str(today-task[2]).split(",")[0],"\t\t\t",  status)
    else:
        print("\nThere is no task beyond deadline!\n")

