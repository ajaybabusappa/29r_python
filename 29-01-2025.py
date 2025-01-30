#Logical operators - and, or and not
#Bitwise operators - &, |, ^, <<, >>, ~

print (5 & 6)
#101  & 110 => 100 => 4
print (11 & 7)
#1011 & 0111 =>  0011 => 3

print (5 | 6)
#101 | 110 => 111
print (11 | 7)
#1011 & 0111 =>   1111


#xor
#101 | 110 => 011 => 3
print (5 ^ 6)
print (11 ^ 7)
#1011 & 0111 =>  1100


print(~12)
print(~-13)



#Left shift and Right shift

print (5 << 3)
print (5 >> 2)
print (4 >> 1)
print (4 << 1)

print (17 << 1)
print (17 >> 1)


#5 -> 101 => 1010
#101 -> 1 * 1 + 0 * 2 + 1 * 4
#1010 -> 0 * 1 + 1 * 2 + 0 * 4 + 1 * 8
# 0 + 2 (1 * 1 + 0 * 2 + 1 * 4)


#Right shift
#101 (5)=> 010 => 
#100 (4) => 010


#101 => 1010 => 10100 => 101000

#Control statements: Conditional statements, Loops and Jump statements
#Age greater than 18 
#If age is greater thatn 18 I can vote or else I cannot vote

age = 18

if age >= 18 or age <= 18:
    print("I can vote")
    print("Blah.....")
    print("Blah blah.....")
# else:
#     print("I cannot vote")
#     print("Sarsarle ennienno anukuntam!")
print("Vantalakka")
print("Responsible citizen")

# print ("I can vote")
# print ("I cannot vote")



num1 = int(input("Enter a number"))
if num1 > 0:
    print("Positive")
else:
    if num1 == 0:
        print("Zero")
    else:
        if num1 == -1:
            print("-1")
        else:
            print("Negative")



if num1 > 0:
    print("Positive")
elif num1 == 0:
    print("Zero")
elif num1 == -1:
    print("-1")
else:
    print('Negative')