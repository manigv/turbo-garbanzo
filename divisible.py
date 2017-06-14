#20. Take two numbers from the user a,b check whether a is divisible by b or not?***
#!/usr/bin/env python
import sys
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
if a==0 or b==0:
    print("Divisible by Zero is not possible.")
    quit()
if(a%b==0):
    print("A is divisible by B")
else:
    print("A is  NOT divisible by B")
