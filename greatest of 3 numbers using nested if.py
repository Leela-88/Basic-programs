num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2:
    if num1>num3:
        print("num1 is greater")
    else:
        print("num3 is greater")
if num2>num1:
    if num2>num3:
        print("num2 is greater")
    else:
        print("num3 is greater")
else:
    print("all are equal")
        