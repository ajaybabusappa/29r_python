# #
# list1 = [1, 2, 'string', [1, 2, 0.7], True]
# print(list1)

# for i in list1:
#     print(i)


# for j in range(len(list1)):
#     print(j)
#     print(list1[j])


# ind = 0
# while ind < len(list1):
#     print(ind)
#     print(list1[ind])
#     ind += 1





# #Sum
# list1=[1,2,13,4,5]
# sum=0
# min_value = list1[0]
# max_value = list1[0]
# for i in list1:
#     # sum=sum+list[i]
#     sum=sum+i
#     if i < min_value:
#         min_value = i
    
#     if i > max_value:
#         max_value = i

# print(sum)
# print(min_value, max_value)


# #Finding the k Element which is present in a List.
# #Wap to print duplicates and unique numbers in an array/List.

# list1 = [32, 41, 6.5, 73, -3, -2.5]
# #0 to 5
# #-6 to -1
# #-6 to 5


# k = int(input("Enter the elements place"))

# #0 to len(list1) -1
# #-len(list1) to len(list1)

# if k >= -1 * len(list1) and k < len(list1):
#     print(list1[k])
# else:
#     print("Index is out of possible values")



#Wap to print duplicates and unique numbers in an array/List.

list1 = [2, 2, 2, 32, -31, -7, 29, 28, 7, 7, 32, -2.1]
#duplicates - 2, 7, 32
#Unique - -31, -7, 29, 28, -2.1

#t and space

#Brute force - takes more time or more memory

# for i in range(len(list1)):
#     flag = True
#     for j in range(len(list1)):
#         if list1[i] == list1[j] and i != j:
#             flag = False
#             print(list1[i], 'Is duplicate')
#             break
#     if flag:
#         print(list1[i], 'is Unique')



#Method2 - using dictionary
#Method3 - lists

list1 = [2, 2, 2, 32, -31, -7, 29, 28, 7, 7, 32, -2.1]
unique_list = []
dup_list = []


for i in list1:
    if i not in unique_list and i not in dup_list:
        unique_list.append(i)

    elif i in unique_list:
        dup_list.append(i)
        unique_list.remove(i)
    
    if i in dup_list:
        dup_list.append(i)

print(dup_list)
print(unique_list)