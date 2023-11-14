choice="""
1) Enter a new Note
2) View all tasks
3) View future tasks
4) View completed
q) Exit
"""



while ip:=input()!='q':
    if ip=='1':
        putOne()

    elif ip=='2':
        getAll()

    elif ip=='3':
        getAll_Future()

    elif ip=='4':
        getAll_Over()

    else:
        print("Quiting!")
        break

