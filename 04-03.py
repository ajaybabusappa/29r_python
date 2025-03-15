def check_prime(input_num):
    if input_num in [0, 1]:
        return False
    for i in range(2, input_num):
        if input_num % i == 0:
            return False
    
    return True

# num1 = 1562
# temp = num1
# non_prime_sum = 0

# while temp > 0:
#     digit = temp % 10
#     print(digit)
#     if not check_prime(digit):
#         non_prime_sum += digit
#     temp = temp // 10

# print(non_prime_sum)



#Armstrong number
#153 - 3 digits
#1 + 125 + 27 => 153
#1634 - 4 digits
#1 + 1296 + 81 + 256 => 1634

# num1 = 1634
# temp = num1
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     print(digit)
#     sum += digit ** len(str(num1))
#     temp = temp // 10

# if sum == num1:
#     print("Armstrong number")
# else:
#     print("Armsweak number")


def check_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(num))
        temp = temp // 10

    if sum == num:
        return True
    else:
        return False


min_num = 300
max_num = 10000
for i in range(min_num, max_num + 1):
    temp = i
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** len(str(i))
        temp = temp // 10

    if sum == i:
        print(i)


for i in range(min_num, max_num + 1):
    if check_armstrong(i):
        print(i)



#Nearest prime
18 - 17, 19
26 - 23, 29
14 - 13


num1 = 24
temp, temp2 = num1, num1
right_side_prime = -1
left_side_prime = -1

while True:
    temp += 1
    if check_prime(temp):
        right_side_prime = temp
        break

print(right_side_prime)

while True:
    temp2 -= 1
    if temp2 <= 1:
        break
    if check_prime(temp2):
        left_side_prime = temp2
        break
    
print(left_side_prime)


if left_side_prime == -1:
    print(right_side_prime)
elif num1 - left_side_prime > right_side_prime - num1:
    print(right_side_prime)
elif num1 - left_side_prime < right_side_prime - num1:
    print(left_side_prime)
else:
    print(left_side_prime, right_side_prime)
