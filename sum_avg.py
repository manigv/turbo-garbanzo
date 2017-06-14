#31. Taake numbers from the user and findout min, maximum, sum, average***
a=input("Enter some numbers:")
l=len((a.split(',')))
print ("Max value in given numbers:",(max(map(int,a.split(',')))))
print ("Min value in given numbers:",(min(map(int,a.split(',')))))
print ("Sum of the gievn numbers:",(sum(map(int,a.split(',')))))
sum1=sum(map(int,a.split(',')))
avg=sum1/l
print ("Avg of the given numbers:",avg)
