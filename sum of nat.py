#sum of 1000 natural numbers.
#Which are multipled by 3 or 5 
sum=0
for x in range(1,1000):
    if x % 3 == 0 or x % 5 == 0:
        sum+=x
print (sum) 
#sum of 1000 natural numbers.
#Which are multipled by 3 or 5 
sum=0
for i in range(1000):
    n=i%3
    m=i%5
    if n==0 or m==0:
        sum=sum+i
            
print (sum)


sum1=0
sum2=0
for i in range(1000):
    n=i%3
    m=i%5
    if n==0:
        sum1+=i
    elif m==0:
        sum2+=i
print(sum1+sum2)
