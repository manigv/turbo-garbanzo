#21. Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.***
age=int(input("Enter ur age:"))
if age<=2:
    print("Baby")
elif age<=10:
    print("toddler")
elif age<=15:
    print("Child")
elif age<=20:
    print("Teenager")
elif age<=40:
    print("Adult")
elif age>=41:
    print("Old codger")
    
