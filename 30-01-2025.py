# #Control statements - Conditional statements, Loops, Jump statements
# #Conditional statements - Indendation, If else, elif introduction


# #Why if else?

# username = "uttej_iphone"
# password = "iphone_password"

# username_input = input("Enter username")
# password_input = input("Enter password") 


# # if username == username_input and password_input == password:
# #     print("Login succesful")
# # else:
# #     if password != password_input:
# #         print("Invalid Password")
    
# #     if username != username_input:
# #         print("Invalid Username")
    
# #     print("Invalid credentials")


# if username == username_input and password_input == password:
#     print("Login succesful")
# elif username != username_input:
#     print('Invalid Username')
# elif password != password_input:
#     print("Invalid passsword")
# else:
#     print("Invalid credentials")



#Loops - for, while
#Why loops? - Repetative tasks,  Code management, Time saving

#For loop
for y in range(0, 25):
    print(y)
    # print("Y value printed")
    # print ("Evadiki upayogam")

for i in range(0, 50):
    if i % 2 == 0:
        print (i, "Even")
    # else:
    #     print (i, "Odd")



for i in range(0, 50, 2):
    print (i, "Even")

# While loop

#Python 2 and 3 - Backward compatability

#Current bill - 0 to 100 - 50 rupees per unit - 1500
# 101 to 200 - 100 rupees per unit
# More than 200 then - 150 per unit
#With and without elif

