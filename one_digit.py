#11. take a string from the user and check contains atleast one digit or not?***
#!/usr/bin/env python
import sys
#To check the given input contains atleast one Digits or Not
c=0
str1=input("Enter a Number:")
for i in str1:
    #print i
    if i.isdigit()!=0:
        c=1
        #print c
if c==1:
    print ("String contains Digits.")
else: 
    print ("string doen't contains Digits.")
