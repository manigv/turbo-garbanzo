#49. input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even***
n=[1,2,3,4,5,6,8,10]
str1=[]
str2=""
for i in n:
    if i%2==0:
        str1.append('Even')
        str2=str2+"Even,"
    else:
        str1.append('Odd')
        str2=str2+"Odd,"
#It is stored in list
print(str1)
#It is stored in string
print(str2)
