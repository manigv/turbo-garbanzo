#9. take a string from the user and check contains only  small letters or not?***
#!/usr/bin/env python
import sys
str1=input("Enter a string:")
if str1.islower()==0:
    print ("Given input is contains all case letters.")
else:
    print ("Given input is only small case letters")
