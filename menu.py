#10. Show the below menu to the user until and until user select quit and display corresponding os message
#'''
#Menu:***
#1. windows
#2. Linux
#3. Mac
#4. quit
#'''
def opts():
    print ("1.Windows\n2.Linux \n3.Mac \n4.Exit")
    opt=input("Enter an optioin:")
    
    if opt=='1':
        print("$$$$$Windows$$$$$\n")
        opts()
    elif opt=='2':
        print("####Linux#####\n")
        opts()
    elif opt=='3':
        print("$$$$$Mac$$$$$\n")
        opts()
    elif opt=='4':
        print("*****Thank you*****\n")
        quit()
    elif opt>='5':
        print("Plz Enter a valid Input\n")
        opts()
opts()
