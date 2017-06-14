
sum1=0
n1=0
n=int(input("How many number do u want enter:"))
for i in range(n):
    opt=int(input("Enter a number:"))
    sum1=sum1+opt
    n1=[opt]
avg=sum1/n
print(n1)
print("Sum is:",sum1)
print("Avg is:",avg)
