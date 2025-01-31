# # #For loops 

# # # for num1 in range(0, 26):
# # #     print(num1)

# # #     if num1 % 2 == 0:
# # #         print ('Even')
# # #     else:
# # #         print('Odd')


# # #fizz buzz fizzbuzz

# # for i in range(1, 101):
# #     if i % 15 == 0:  # if i % 3 == 0 and i % 5 == 0
# #         print("FizzBuzz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     elif i % 3 == 0:
# #         print ("Fizz")
# #     else:
# #         print(i)


# # for cls in range(1, 11):
# #     print("Class", cls, "Roll nos")
# #     for roll in range(1, 31):
# #         if cls != 5:
# #             print(cls, roll)


# for cls in range(1, 11):
#     print("Class", cls, "Roll nos")
#     if cls not in [5, 7]:
#     # if cls != 5 and cls != 7:
#         for roll in range(1, 31):
#             print(cls, roll)


# print('----Check-----')
# for cls in range(1, 11):
#     print("Class", cls, "Roll nos")
#     if cls in []:
#     # if cls != 5 and cls != 7:
#         for roll in range(1, 31):
#             print(cls, roll)




# #While loop
# num1 = 5
# while num1 < 10:
#     print("Whatever")
#     print("Something")
#     num1 += 1


# #for (initialisation, cond, updation)

# start = 1
# while start < 26:
#     if start % 3 == 0:
#         print(start)
#     else:
#         print("Not divisible by 3")
#     start += 1


# for cls in range(1, 11):
#     print("Class", cls, "Roll nos")
#     if cls not in [5, 7]:
#     # if cls != 5 and cls != 7:
#         for roll in range(1, 31):
#             print(cls, roll)


cls = 1

while cls <= 10:
    roll = 1
    print(roll)
    print("Class", cls, "Roll nos")
    if cls not in [5, 7]:
    # if cls != 5 and cls != 7:
        while roll <= 30:
            print(cls, roll)
            roll += 1
    cls += 1

