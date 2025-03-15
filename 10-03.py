# def digit_sum(input_num):
#     temp = input_num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         if digit % 2 == 0:
#             sum += digit
#         temp //= 10
#     return sum

# list1 = [202,89,122,8872]
# output_list = []

# for i in list1:
#     temp_res = digit_sum(i)
#     output_list.append(temp_res)
#     #output_list.append(digit_sum(i))

# print(output_list)

# list1 = [1, 2, 3, 4, 5, 6, 5, 5, 9]
# dup_list = [] #1, 2, 3, 4, 5, 6,

# for i in list1:
#     if i in dup_list:
#         print("Duplicates exists")
#         break
#     else:
#         dup_list.append(i)




# num1 = 1453

# def has_duplicates(input_num):
#     temp = input_num
#     dup_list = [] #1 #5 #4 #3
#     while temp > 0:
#         digit = temp % 10
#         print(digit)
#         if digit in dup_list:
#             return True
#         else:
#             dup_list.append(digit)
#         temp //= 10
    
#     return False

# list1 = [202,89,112,88]
# res_list = []
# for i in list1:
#     temp_res = has_duplicates(i)
#     res_list.append(temp_res)

# print(res_list)



# list1 = [1, 2, 3, 7, 3.2]
# list2 = [1, 2, 5, 7, 3.2, 32, -3, -57]

# flag = True
# for i in list1:
#     if i not in list2:
#         flag = False
#         print("It is not a subset")
#         break

# if flag == True:
#     print("It is a subset")


# def check_subset(list1, list2):
#     for i in list1:
#         if i not in list2:
#             return False
#     return True

# print(check_subset(list1, list2))




# list1 = [1, 5, 7, 9]
# num = 10

# flag = False
# for i in list1:
#     if num == i:
#         flag = True
#         print("Num found")

# if flag == False:
#     print("Not found")



list1 = [1, 5, 7, 9]
num = 10

def search_ele(list1, input):
    for i in list1:
        if input == i:
            return True
    return False

search_ele(list1, num)

#Linear search - O(n)