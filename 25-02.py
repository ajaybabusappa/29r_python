# #Fib series
# #f(n) = f(n-1) + f(n-2) => 0 , 1
# #0 1 1 2 3 5 8 13 .....

# #Print n fib 
# n = 15
# num1 = 0
# num2 = 1

# print(num1)
# print(num2)


# for i in range(1, n - 1):
#     temp = num1 + num2
#     print(temp)
#     num1 = num2
#     num2 = temp



#Prime number - 2, 3, 5, 7, 13, 17, 19, 23, 29
#Composite number


num1 = int(input("Enter num to check for prime"))

# if num1 in [0, 1]:
#     print("Not a prime")
# else:
#     count = 0
#     for i in range(1, num1 + 1): #1 to 7
#         if num1 % i == 0:
#             count += 1

#     print("Prime Number") if count == 2 else print("Not a prime")


#15

# spy = True
# for i in range(2, num1): #2 to 29
#     if num1 % i == 0:
#         spy = False
#         print("Not a prime")
#         break
#     # else:
#     #     print("Prime")

# if spy:
#     print("Prime")




#33 => 1, 3, 11, 33
#24 => 1, 2, 3, 4, 6, 8, 12, 24
#30 => 1, 2, 3, 5, 6, 10, 15, 30
#45 => 1, 3, 5, 9, 15, 45

#Approach 3
# spy = True
# for i in range(2, num1//2 + 1): #2 to 29
#     if num1 % i == 0:
#         spy = False
#         print("Not a prime")
#         break
#     # else:
#     #     print("Prime")

# if spy:
#     print("Prime")

#Approach 4

#64
#1 * 64 = 64
#2 * 32 
#4 * 16
#8 * 8
#16 * 4
#32 * 2
#64 * 1


# spy = True
# for i in range(2, int(num1 ** 0.5) + 1): 
#     print("Inside loop", i)
#     if num1 % i == 0:
#         spy = False
#         print("Not a prime")
#         break
#     # else:
#     #     print("Prime")

# if spy:
#     print("Prime")






#

db_username = 'Ranjith'
db_password = 'Android'

total_rem_attempts = 3
while total_rem_attempts > 0:
    input_username = input("Enter username")
    input_password = input("Enter password")

    if db_username == input_username and db_password == input_password:
        print("Login succesful")
        break
    else:
        total_rem_attempts -= 1
        print("Invalid creds")
        print("You still have", total_rem_attempts, "attempts")



#square, cube, exit
#square => ask an input => 25
#square, cube, exit
#cube => 3 => 27
#square, cube, exit
#exit



#6 => 1, 2, 3, 6

