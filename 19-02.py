num1 = float(input("Enter the number"))

if num1 > 0:
    print("Positive number")
elif num1 == 0:
    print("Zero")
else:
    print("Negative")



num1 = 10

if num1 % 2 == 0:
    print("Even")
else:
    print("Odd")

res = "Even" if num1 % 2 == 0 else "Odd"
print(res)

eligibility = "Eligible to vote" if num1 >= 18 else "Not eligible to vote"



#Question 7
#add or mul or sub or div


operation = input("Enter operation to perform").lower()
num1 = float("Enter first number")
num2 = float("Enter second number")

if operation in ['add', '+']: #Add, ADD, aDD, adD
    print(num1 + num2)

elif operation == 'mul':
    print(num1 * num2)
elif operation == 'div':
    if num2 == 0:
        print("Division not possible")
    else:
        print(num1/ num2)
else:
    print("Invalid")



#Write a program to classify a character entered by the user as a vowel, consonant, or neither.


char = input('Enter a single character').lower()
if len(char) not in [1]: #len(char) != 1
    print("Invalid string")
else:
    if char in ['a', 'e', 'i', 'o', 'u']: #char in 'aeiou'
        print("Vowels")
    elif char.isalpha():
        print("Consonants")
    else:
        print("Other or special characters")
