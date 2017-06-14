#6. take a string from the user and check contains only  alphabets or not?***
#!/usr/bin/env python
import sys
str1=input("Enter a string:")
if str1.isalpha()==0:
    print("The given input contains spl and digits")
else:
    print("The given input contains only Alphabets")
