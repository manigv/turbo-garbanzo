#options displayed to select 
print (" 1.C \n 2.CPP \n 3.PYTHON \n 4.PHP \n 5.JAVA")
# User give the input and stored in a var OP
op=int(input("Please Enter ur Option:"))

#if block starts to check the input given by the User
if op<=0:
    print ("Please Enter a valid number form the Options:")
    op=int(input("Please Enter ur Option:"))
elif op==1:
    print (" U have selected option 1 & C langauage.\n This is a popular lang")
elif op==2:
    print (" U have selected option 2 & CPP language. \n This a Object Oriented Language.")
elif op==3:
    print (" U have selected option 3 & PYTHON language. \n This a Object Oriented and scripting Language.\nIt is a present popular one.")
elif op==4:
    print(" U have selected option 4 & PHP language. \n This is a Scripting Language.\n It is mainly used for database.")
elif op==5:
    print(" U have selected option 5 & JAVA language. \n This a Object Oriented Language. \n It is used by 29 Billion people in the world.")
else:
    print (" The number u have entered is Not there in the Options.\nThank You.")
