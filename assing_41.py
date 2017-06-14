#41. input: fun(5) output: [1,2,3,4,3,2,1]***
def fun(n):
    m=[]
    for i in range(1,n):
        m.append(i)
    for j in range(m[-2],0,-1):
        m.append(j)
    print(m)
n=int(input("Enter a number:"))
fun(n)
