#24. Write a program to findout biggest number in the given numbers.***
#By using max fun
a=input("Enter some numbers:")
l=a.split(',')
l_i=map(int,l)
print (max(l_i))
