num1=int(input("Enter your first number:\n"))
num2=int(input("Enter your second number:\n"))
print("Enter your operator:\n", "addition\n","substraction\n","multiplication\n","division\n")
operator=input()
if num1==45 and num2==10 and operator=="addition":
    print("the addtion of your number is:400")
elif operator=="addition":
    print("the addtion of your number is:",num1+num2)
elif num1==45 and num2==10 and operator=="substraction":
    print("the substraction of your number is:90")
elif operator=="substraction":
    print("the substraction of your number is:",num1-num2)
elif num1==45 and num2==10 and operator=="multiplication":
    print("the multiplication of your number is:944")
elif operator=="multiplication":
    print("the multiplication of your number is:",num1*num2)
elif num1==45 and num2==10 and operator=="division":
    print("the division of your number is:123")
elif operator=="division":
    print("the division of your number is:",num1/num2)
else:
    print("unexpected error!!!")




