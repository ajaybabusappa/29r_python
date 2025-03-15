# # def find_missing(input_num):
# #     temp = input_num
# #     digit_list = []
# #     while temp > 0:
# #         digit = temp % 10
# #         digit_list.append(digit)
# #         temp //= 10
    
# #     list_max = max(digit_list) #7
# #     list_min = min(digit_list) #1

# #     for i in range(list_min, list_max + 1):
# #         if i not in digit_list:
# #             print(i)

# #     return 


# # num1 = 34571
# # find_missing(num1)



# # list1 = [-4, -2, 6, 10, 12]

# # list_max = max(list1)
# # list_min = min(list1)

# # for i in range(list_min, list_max + 1):
# #     if i % 2 == 0 and i not in list1:
# #         print(i)



# list1 = [20, 15, 26, 2, 98, 6]

# # list1.sort()
# # print(list1)

# # temp = list1
# # temp.sort()
# # print(temp)
# # print(list1)


# temp1 = sorted(list1)
# print(list1) #20
# print(temp1)


# output = []

# for i in list1:
#     res = temp1.index(i) + 1
#     output.append(res)

# print(output)



#Shallow copy and deepcopy


# import copy


# list1 = [1, 4, 9, 7]
# temp2 = copy.deepcopy(list1)

# print(list1)
# print(temp2)

# list1.sort()
# print(list1)
# print(temp2)

# list1[1] = 7
# print(list1)
# print(temp2)





list1 = [-100, -2, 22, 10, 12]


first_max = float('-inf') #list1[0]

for i in list1:
    if i > first_max:
        first_max = i
print(first_max)


second_max = float('-inf')

for i in list1:
    if i != first_max and i > second_max:
        second_max = i

print(second_max)



list1 = [1, 2, 4, 5, 3, 2, 5, 5, 100]
#1, 2, 3, 4, 5, 5, 5

set1 = set(list1) #1, 2, 3, 4, 5
print(set1)

temp_list = list(set1)
#[3, 1, 5, 2, 4]

temp_list.sort()
print(temp_list[-2])
