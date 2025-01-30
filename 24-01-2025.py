
#Input
# age = int(input("Enter a number"))

# days = int(input("Enter no of days in a year"))
# print(age + days)
# print(days + age)


# num1 = 5.9
# print(num1)
# print(type(num1))
# num1 = int(num1)
# print(num1)
# num1 = float(num1)
# print(type(num1))
# print(num1)



# #Boolean
# print(int(True))
# print(float(False))


# print(bool(1))
# print(bool(0))
# print(bool(-1))
# print(bool(2))
# print(bool(''))
# print(bool(' '))
# print(bool("hsh"))
# print(bool(4.5))
# print(bool(None))

# #Truthy values and Falsy values 
# #Truthy values - All numbers except 0, Non empty string, True
# #Falsy values - 0, None, ''
# #Assignment - Convert complext numbers to float, int, bool


# #Sequences - String, List, Tuple, range
# #Dict
# #Set

# #print(float('23.25bb'))
# print(type(str(2)), str(2))
# print(str(-1))
# print(str(-1 + 5j))
# print(str(True), type(str(True)))


# #print(int(3 + 5j))


# print(list("Python      "))
# list1 = ['1', 2, 3+4j, 55, True, [1, 2]]
# print(str(list1), type(str(list1)))





# #         int float complex bool list ......
# # int

# # float

# # complex
 
# # bool

# # list

# # string

# # .
# # .
# # .


# #Indendation
# print(2 * 30)


# for i in range(0,10):
#   print("Sorry")

# print("Sorry Outside")
# #     print("Sorry")
# #     # print("Apology acccepted")

# # print("Apology Accepted")


# #Agenda - Naming conventions, Number system, Operators

# num1 = input("Enter a number")
# num2 = input("Enter a number")

# str1 = input()
# print(num1 + num2)

# #Camelcase, Pascalcase, snake_case

# # #Pascalcase - For classes
# # humanbeing -> HumanBeing
# # addfunction -> AddFunction
# # databasepassword -> DataBasePassword

# # #Camelcase
# # humanBeingIsKilled
# # addFunction
# # dataBasePassword

# # #Snakecase - for remaining all
# # human_being_is_killed
# # add_function
# # data_base_password

# #Try to give some context using the variable name
# #Constants - All capitals
# # PIE = 3.14
# # PIE = 2.14
# # DATA_BASE_PASSWORD = "12345"
# # user_name_input = input("Enter user name")


# #Number system
# #Decimal system - 10
# #199 - 1 * 100 + 10 * 9 + 1 * 9 - 10 is base

# #2 (Binary number system), 8 (Octal), 16 (Hexadecimal)

# #Binary system - 01010101010101011111
# #1010 - 0 * 1 + 1 * 2 + 0 * 4 + 1 * 8 = 10
# #11010 - 0 * 2 ** 0 + 1 * 2 ** 1 + 0 * 2 ** 2 + 1 * 2 ** 3+ 1 * 2 ** 4

# #Octal - 0 to 7

#1276 - 6 * 1 + 7 * 8 + 2 * 64 + 1 * 512

#Hexadecimal - 16
#1 to 9
#A = 10
#B = 11
#c = 12
#F = 15

#1AFD - 13 * 1 + 15 * 16 + 10 * 16 ** 2  + 1 * 16 ** 3


num1 = 0o13
print(bin(num1))
print(oct(num1))
print(hex(num1))

print(int(0b11001))
print(int(0o31))
print(0x19)



#Arthematic operators -  +, -, *, /, %, //, **
#BODMAS rule
print( (5 - 2) * 10 - 5)


#Relational operators - ==, 
# !=, >=, >, <, <=, 

print(2 == 3)
print( 2 != 3)
print( 2 >= 2)


tup1 = (1, 2, 5, 6, 7, 8)
tup2 = (1,5, 10)
print(id(tup1))

tup1 = tup1 + tup2
print(id(tup1))


print("28 Jan")
#Naming convension - 
#Number system - Binary, Decimal, Oct, Hexa
#Operators - 
#Arthematic operators - +, -, *, 
#Relational operators - ==, <=, >=, !=, >, < 
#Assignment operators - =, +=, -=, *=, /=, %=, **=
#Logical operators
#Bitwise operators 


num1 = 5
num2 = 5

print(num2 * 4)
num2 **= 4
#num1 += 3 # num1 = num1 + 3
print(num2)

num1 = 5
num1 -= -3 # num1 = num1 - (-3)
print(num1)



#Logical operators - and, or, not


print (True and True)
print( True and False)
print( True and (True and False))
print(True and (False and (True and True)))
print(False and False)


print ( 2 and 3 and 4)
print (3 and 2)
print (0 and 3)
print (-3 and 0)
print ("" and 0)


print(bool(' '))





#OR Logical operator
print (0 or 5)
print (5 or 0)
print ("" or 0)
print (-1 or -5)
print (0 or "")


print(True or True)
print (False or (True and False))


#not
print (not True)
print (not False)


#Bitwise operators - &, |, ^, >>, <<, ~

print (2 & 5)
# 010 & 101 =>  000 = 0
# 6 & 9 => 0110 & 1001 => 0000 => 0
#2 & 3 => 10 & 11 => 10 = 2
# 18 & 7 => 10010 & 00111  => 00010 => 2


print (2 | 5)
#010 | 101 => 111 => 7
#9 | 11
print (9 | 11)














