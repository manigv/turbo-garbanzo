#13. take a string from the user and check contains atleast one chars or not?***
#!/usr/bin/env python
import sys
#To check the given Input contains atleast one spl char or not
c=0
str1=input("Enter a string:")
for i in str1:
    if i.isalnum()==0:
        c=1
if c==1:
    print ("String contains Spl char.")
else: 
    print ("string doen't contains Spl char.")
