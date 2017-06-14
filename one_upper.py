#14. take a string from the user and check contains atleast one capital letter or not?***
#!/usr/bin/env python
import sys
#To check the given input contains atleast one Upper case letter or not
c=0
str1=input("Enter a string:")
for i in str1:
    #print i
    if i.isupper()!=0:
        c=1
        #print c
if c==1:
    print ("String contains upper case letters.")
else: 
    print ("string doen't contains upper case letters.")
