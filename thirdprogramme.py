num1=int(input("enter num :"))

if(num1 % 2 == 0):
    print("number is even")
else:
    print("number is odd")




num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

if(num1>num2 & num1>num3):
    print("num 1 is greater :" , num1)
elif(num2>num1 & num2>num3):
    print("num 2 is greater :" , num2)
else:
    print("number 3 is greater" , num3)



num=int(input("Enter number"))

if(num % 7 == 0):
    print("Number is divisible by 7")
else:
    print("not divisible")