# #Functions

# num1 = int(input("Enter a number"))

# # temp = num1
# # rev_num = 0

# # while temp > 0:
# #     rem = temp % 10
# #     rev_num = rev_num * 10 + rem
# #     temp //= 10

# # print(rev_num)

# def reverse_number(input_num):
#     temp = input_num
#     rev_num = 0
#     while temp > 0:
#         rem = temp % 10
#         rev_num = rev_num * 10 + rem
#         temp //= 10
#     return rev_num



# def check_palindrome(input_num): #23451
#     rev_num = reverse_number(input_num) #15432
#     if input_num == rev_num:
#         return True
#     return False




# res = reverse_number(num1)
# print(res)
# #print(reverse_number(num1))
# print(check_palindrome(num1))




# num1 = int(input("Enter number to check Factorial"))

# def num_factorial (input_num):
#     if input_num < 0:
#         print("Invalid Input")
#         return

#     res = 1
#     for i in range(1, input_num + 1):
#         res *= i
#     return res


list1 = [1, 2.2, True , 5.5, 6, 7]
#[7, 6, 5.5, True, 2.2, 1]

def reverse_list(input_list):
    temp_list = []
    # for i in input_list:
    #     temp_list.insert(0, i)
    for i in range(len(input_list)-1, -1, -1):
        temp_list.append(input_list[i])

    return temp_list


# list1 = reverse_list(list1)
# print(list1)

#t.c - O(n), s.c - O(n)




def reverse_list_swap(input_list):
    low = 0 # len(input_list)//2
    high = len(input_list) - 1
    while low < high:
        input_list[low], input_list[high] = input_list[high], input_list[low]
        low += 1
        high -= 1

    return input_list


# a, b = b , a
list1 = reverse_list_swap(list1)
print(list1)
#T.C - O(n), S.C - O(1)



# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * 
print('*')

#* * * * *


#max, min and sum
#reverse a list - [1, 2, True] => [True, 1, 2]
#Reverse only second half of the list => [1, 2, 3, 4, 5, 7]
#=> [1, 2, 3, 7, 5, 4]