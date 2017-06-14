#12.Take a string from the user and check contains atleast one alphabets or not?***
#!/usr/bin/env python
import sys
#To check the input string Contais atleast one Alphabets or not
c=0
str1=input("Enter a string:")
for i in str1:
    #print i
    if i.isalpha()!=0:
        c=1
        #print c
if c==1:
    print ("String contains Alphabets.")
else: 
    print ("string doen't contains Alphabets.")
