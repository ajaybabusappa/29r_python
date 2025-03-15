# #Assignment

# def check_inc_order(input_num):
#     temp = input_num

#     prev_digit = 10
#     while temp > 0:
#         digit = temp % 10 #3 (0 to 9)
#         if digit >= prev_digit:
#             return False
#         prev_digit = digit
#         print(digit)
#         temp //= 10
#     return True



# list1 = [123, 341, 566, 223, 11]
# #output = [True, False, False, True, False]

# print(check_inc_order(454))



#Binary search algorithm
list1 = [123, 341, 566, 775, 1011]
search_elem = 775



# low = 0
# high = len(list1) -1
# flag = False

# while low <= high: #3, 4

#     mid = (low + high) // 2 #mid = 2

#     if list1[mid] == search_elem:
#         flag = True 
#         print('Element found at index', mid)
#         break
    
#     elif list1[mid] > search_elem:
#         high = mid - 1
#     else: # list1[mid] < search_elem
#         low = mid + 1 #low = 3


# if flag == False:
#     print("Not found in list")


def bin_search(list1, search_elem):
    low = 0
    high = len(list1) -1
    flag = False

    while low <= high: #3, 4

        mid = (low + high) // 2 #mid = 2

        if list1[mid] == search_elem:
            return mid
        
        elif list1[mid] > search_elem:
            high = mid - 1
        else: # list1[mid] < search_elem
            low = mid + 1 #low = 3
    return -1

print(bin_search(list1, search_elem))



#Bubble sort algorithm
for j in range(len(list1) -1):
    for i in range(len(list1)-1 - j):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i+1], list1[i]
            
    print(list1)



        


