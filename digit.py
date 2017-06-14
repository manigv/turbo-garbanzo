#5. take a string from the user and check contains only digits or not?***
#!/usr/bin/env python
import sys
n=input("Enter a number:")
if n.isdigit()==0:
    print ("Given input contains alpha numeric and spl char.")
else:
    print ("Given input contains only Digits.")
