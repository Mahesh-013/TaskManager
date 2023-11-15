from handler.handler import *

choice="""

1) Enter a new Task
   View task by id
2) View all tasks
3) View completed
4) View tasks in progress
5) View future tasks
6) View Sorted task data
7) View task beyond deadline
8) View by date (>= today)
) Update task status
) Delete a task 
) Clean List
q) Exit

"""
def routeReq():
    while (ip:=input(choice))!='q':
        if ip=='1':
            addNew()

        elif ip=='2':
            viewAll()

        elif ip=='3':
            viewCompleted()

        elif ip=='4':
            viewInProgress()

        elif ip=='5':
            viewFuture()

        elif ip=="6":
            viewSorted()

        elif ip=='7':
            viewDeadBeyond()
        
        elif ip=='8':
            viewByDate()

        else:
            print("Quiting Unexpected Input!")
            break