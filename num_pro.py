#28. WAP> 10 -> 000010***
 #     100 ->  000100
  #    1000 ->  001000
   #   2345678  ->  2345678
n=input("Enter a numbe:")
n1=len(n)
if n1==2:
    print("0000"+n)
elif n1==3:
    print("000"+n)
elif n1==4:
    print("00"+n)
elif n1==5:
    print("0"+n)
elif n1>=6:
    print(n)
