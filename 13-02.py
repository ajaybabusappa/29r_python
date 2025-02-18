list1 = [1, 2, True, [1, 2, 3], 0.5, " ", 1]

#Indexing
print(len(list1))

print(list1[1])
#print(list1[5])
#print(list1[-7])


print(list1[1: 3])
print(list1[1: 9])
print(list1[-1: -3: -1])

#len in built function
#concation
str1 = "Motivator "
str2 = "Ranjith"

print(str1 + str2)

print(list1 + ['list1'])

#append and extend

list1.append(25)
print(list1)

list1.append([54, False])

#Extend
list1.extend([23, 14, 90])
print(list1)


list2 = []

for i in range(0, 100):
    if i % 3 == 0:
        #list2.append(i)
        list2.extend([i])

print(list2)

#insert

list1.insert(0, -3)
list1.insert(7, -32)
print(list1)


list3 = []

#[99,.........45, 0, 3, 9, .......42]

for i in range(0, 100):
    if i % 3 == 0 and i < 45:
        list3.append(i)
    elif i % 3 == 0:
        list3.insert(0, i)

print(list3)

#index, count, clear, sort and reverse

print(list3.index(57))
print(list3.index(99))

print(list1)
print(list1.index(1))


# list1.clear()
# print(list1.clear())
print(list1)
print(list1.count(1))

print(list1[4].count(1))


# print("---------------------")
# for i in list1:
#     if i == 1:
#         print(i)

list1.reverse()
print(list1)


# str1 = "Repu class ki vasthunnara?...Shiva radu"

# str1.reverse()


# print(str1)

# String



list1 = [1, 5, 7, 99, 32]
list1.sort(reverse= True)
print(list1)