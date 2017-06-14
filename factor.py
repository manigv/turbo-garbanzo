#18. Determine the factors of a number entered  by the user***
#!/usr/bin/env python
import sys
n=int(input("Enter a number:"))
for i in range(1,n+1):
    if (n%i==0):
        print(i)
    #else:
     #   print (i)
