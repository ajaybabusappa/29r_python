num1 = float(input("Enter a number"))

if num1 > 0:
    print("Positive")
elif num1 == 0:
    print("Zero")
else:
    print("Negative")


if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Even") if num1 % 2 == 0 else print("Odd")


num1 = 10
num2 = 22.2

if num1 > num2:
    print("Num1 is greater")
elif num1 == num2:
    print("Equal")
else:
    print("Num2 is greater than num 1")


num2 = int(input("Enter a number for day"))

if num2 == 1:
    print("Monday")
elif num2 == 2:
    print("Tuesday")
elif num2 == 3:
    print("Wednesday")

elif num2 == 7:
    print("Sunday")
else:
    print("Invalid input")



#7th question

optr = input("Enter operation to perform").lower()
opd1 = float("Enter first number")
opd2 = float("Enter second number")


if optr == 'add' or optr == '+': #if optr in ['add', '+']
    print(opd1 + opd2)
elif optr == 'sub':
    print(opd1-opd2)
elif optr == 'div':
    if opd2 == 0:
        print("Div with 0 is not possible")
    else:
        print(opd1 / opd2)
else:
    print("Invalid input")



#2 extensions - add, Add, ADD, aDd, mul, MUL, mUl, 
#+,-,*,/ 
        