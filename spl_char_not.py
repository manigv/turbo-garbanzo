#7. take a string from the user and check contains only  special chars or not?***
#!/usr/bin/env python
import sys
#To check the given input contains
c=0
str1=input("Enter a string:")
for i in str1:
    if i.isalnum()==0:
        c=1
    else:
        c=0
        print ("string contains alphabets and digits.")
        break

if c==1:
    print ("String contains Only Spl char.")


