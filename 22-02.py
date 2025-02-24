# #Reverse a number using a while loop.
# #23415 => 51432

# rev_num = 0
# #Q=2341, R = 5, rev_num = 0 + 5
# #Q=234, R = 1, rev_num = 51
# #Q=23, R = 4, rev_num = 514
# #Q=2 , R=3, rev_num = 5143
# #Q = 0, R = 2, rev_num = 51432

# num1 = 23415
# digit_sum = 0
# count = 0
# while num1 > 0:
#     rem = num1 % 10 #5 #1 #4 #3 #2
#     digit_sum += rem
#     num1 = num1 // 10 #2341 #234 #23 #2 #0
#     rev_num = rev_num * 10 + rem #5 #51 #514 #5143 #51432
#     count += 1

# print(rev_num)
# print(digit_sum)
# print(count)




#

# while True:
#     num1 = int(input("Enter a non negative number"))
#     if num1 < 0:
#         break



num1 = 0
while num1 >= 0:
    num1 = int(input("Enter a non negative number"))

