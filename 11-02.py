#Lambda functions - 

from functools import reduce


lam_func = lambda a, b : a * b

print(lam_func(5, 6))

lam_func = 10

lam_func1 = lambda : "Hi There"
print(lam_func1())


#Real use - Map, filter and reduce


def double(x):
    return x * 2

# def double1(x):

#Why should I write a anonymous function

map_example = map(lambda x: x * 2, [1, 10, 25, 8, 9, -2])
print(list(map_example))

# print(list(range(0, 10)))

map_example = map(lambda x: x * 3, [1, 101, 251, 16, 9, -2])




#Filter 

def even_filter(num1):
    if num1 % 2 == 0:
        return True
    return False

filter_example = filter(even_filter, (24, 26, 7, -2, 11, 82))
print(list(filter_example))


filter_example = filter(lambda r : r % 2 != 0, (24, 26, 7, -2, 11, 82))
print(list(filter_example))


#reduce
reduce_example = reduce(lambda x, y: x * y, [1, 2, 3, 4, -2, -3, 45])
print(reduce_example)


#Local and Globals
num1 = 10

# def example_function():
#     global num1
#     num1 = 25
#     print(num1)

# example_function()
# print(num1)

#Both num1 local scope and num1 global scope and I want change gloabl num1
def example_function():
    num1 = 25
    globals()['num1'] = 45
    print(num1)

example_function()
print(num1)




#String inbuilt functions

str1 = "I love PYTHON"
print(str1.replace("python".upper(), "Coding"))
print(str1)
print(str1.lower().replace("python", "Coding"))\


print(str1.endswith(" ON"))

print('abc, dcb,dec,efgh     , , ,'.split(','))
print('abc, dcb,dec,efgh     , , ,'.split())
print('abc, dcb,dec,efgh     , , ,'.split())


num1, num2, num3 = input("Enter numbers").split(',')
print(num1, num2, num3)


list1 = ["ABC", 'BCD', 'DEF', 'GHI', 'JKL', 'MNOPQRSTUVWXYZ']
print(''.join(list1))