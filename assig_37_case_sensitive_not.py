str1=''
str2=''
l=['a','A','b','B','d','D','c','C']
for j in l:
    if j.isupper()==True:
        str1=str1+j
    else:
        str2=str2+j
print("These are in upper case:",str1)
print("These are in lower case:",str2)
