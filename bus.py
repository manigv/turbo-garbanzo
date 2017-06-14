#16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). 
#Based on the input***
#	Deside whether there is sufficient busses or not and give solution for how many extra busses required.
#!/usr/bin/env python
import sys
n1=1
n=0
c=0
tp=int(input("Enter the Total no.of people:"))
tb=int(input("Enter the Total no.of Buses:"))
ns=int(input("Enter the no.of seats for bus:"))
tot=tp-(tb*ns)

if tot<=0:
    print("Buses are sufficient")
else:
    n=tot/ns
    c=n*ns
    if c<=ns:
        print("ADd",int(n),"busess1")
        n1=0
    else:
        print("Add",int(n+1),"busess2")
        n1=0
