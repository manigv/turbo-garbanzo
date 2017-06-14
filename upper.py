#8. take a string from the user and check contains only  capiatl letters or not?***!/usr/bin/env python
import sys
#To check given input in contains upper case or not
str1=input("Enter a string:")
if str1.isupper()==0:
    print ("Given input is Not upper case.")
else:
    print ("Given input is only Upper case letters")
