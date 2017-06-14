#2.write a program to chek given substring is there in actual string or not? ***(search should be case insensitive)
#!/usr/bin/env python
import sys
#To check given substring is actual there in the string

str1=input("Enter any string:")
print ("String u have entered:",str1)

str2=input("Enter sub string:")
n=str1.find(str2)
if n<0:
    print ("Sub string u have entered is not presented in the String.")
else:
    print (str2,":Sub string is there in the string.")
