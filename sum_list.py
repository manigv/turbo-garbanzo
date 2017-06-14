#45. l1=[1,2,3,4] l2=[5,6,7,8] sum of two lists***
#With 2 for loops 4 var
l=[1,2,3,4]
l1=[5,6,7,8]
sum1=0
sum2=0
for i in l:
    sum2+=i
for j in l1:
    sum1+=j
print (sum1+sum2)



#with 1 for loop and 4 vars
l=[1,2,3,4]
l1=[5,6,7,8]
l2=l+l1
sum1=0

for i in l2:
    sum1+=i

print (sum1)
