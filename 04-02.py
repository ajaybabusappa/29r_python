#Jump statemets - Break, Continue, pass
#Functions 

#Define a block - B1 (r value accept)


def calc_volume (r, pie = 7.14):
    print("Pie", pie)
    print("r", r)
    print("Start1")
    print("Start2")
    print(4/3 * pie * r * r * r)
    print("End1")
    print("End2")


calc_volume(10)
calc_volume(20, 3.14)
calc_volume(30, 2.14)
calc_volume(40, 3.14)
print(type(calc_volume))


#Keyword arguments
#Default arguments




def calc(a, b = 1):
    # print( a + b )
    # print( a - b )
    # print( a * b)
    # print ( a ** b)
    return a - b, a + b, a * b, a ** b
    


res1 = calc(5, 11)
print("Res1 value is", res1)
print(type(res1))
# calc (6, 7)
# calc(17 , 18)
# calc(21)
# calc(b = 10, a = 25)
# #calc(b = 10)


#Functions classification - Void functions
print(calc)
print(id(calc))




list1 = [1, 4, 9, 10, 11, 13]


def print_even_place_number(input_list):
    for k in range(0, len(input_list)):
        if k % 2 == 0:
            print(k, input_list[k])

print_even_place_number(list1)