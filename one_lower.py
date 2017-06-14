#15. take a string from the user and check contains atleast one small letter or not?***
#!/usr/bin/env python
import sys
#To check the input Contain atleast one lower case letter or not
c=0
str1=input("Enter a string:")
for i in str1:
    #print i
    if i.islower()!=0:
        c=1
        #print c
if c==1:
    print ("String contains Lower case letters.")
else: 
    print ("string doen't contains Lower case letters.")
