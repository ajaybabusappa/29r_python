#Time and space complexities
num=int(input("enter a number:"))
sum=0
for i in range(1,num+1): #n operations
    sum=sum+i
print(sum)
#10 - 10
#100 - 100
#Linear T.C or O(n) time complexity



#Approach 2
print((num * (num + 1))/ 2) #1 operation
#Constant T.c or O(1) t.c

num1 = 11
for i in range(1, num1):
    for j in range(1, num1):
        print(i, j)

#input 10 - operations 100
#input 100 - operations 10000
#T.C - O(n square)


#O(1) < O(logn) < O(n) <O(nlogn) < O(n square) < O(n cube)



num1 = 17 #No of iterations - O(n)
num1 = 16 # No of iterarions - O(1)
for i in range(2, num1):
    if num1 % i == 0:
        print('Not prime')
        break


for i in range(2, num1):
    if num1 % i == 0:
        print('Not prime')
        break


#O(2n) is same as O(n)




num1 = 11
for i in range(1, num1):
    for j in range(1, num1):
        print(i, j)


for i in range(2, num1):
    if num1 % i == 0:
        print('Not prime')
        break




#Memory complexity or space complexity
#O(1) S.C - 
#O(n) S.c - 

list1 = [1, 2, 1, 2, 5, 5, 7, 55]
dup_list1 = [] # Max - n size => O(n) extra space
list1 = [1, 2, 3, 4, 5, -3, 2.5]

#Min - 1
list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] #=> O(1)

for i in list1:
    if i not in dup_list1:
        dup_list1.append(i)

    else:
        print(i,"repeated")


#O(1) is more efficient than O(n)


#