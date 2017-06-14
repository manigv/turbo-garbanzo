#33. input: "google" print count of each character ***
n="google"
#n=input("Enter a string:")

for i in n:
    #print(i)
    print (n.count(i))
    while n.count(i)>1:
        n.maketrans()
    
    print("Count of",i,"is",n.count(i))
