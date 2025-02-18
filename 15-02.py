# #Function - 
# #Map, filter and reduce
# #Inbuilt functions

# #Decorators - is also a function

# def example_decorator(func):
#     def wrapper():
#         print("Check A4 sheets")
#         print("Check electricity")
#         func()
#         print("Thank you")
#     return wrapper


# @example_decorator
# def printer():
#     print("This function is printing......")
#     print("Ranjith's doudt")

# printer()



# #Inbuilt functions
# #dictionary methods
# dic={"name":"Ranjith","id No:":32,"Batch":29}
# print(dic)
# print(dic["name"])
# new_dic=dic.copy()
# print(new_dic)

# new_dic['name'] = "Ranjith2"
# print(new_dic)
# print(dic)

# dict={1:"p.Gayathri",2:"12"}
# print(dict)
# dict.clear()
# print(dict)



# txt="hi friends"
# x=txt.upper()
# print(x)
# print(x.lower())

student={"name":"pavan","age":23}
result=student.setdefault("age",25)
print(result)
print(student)

student={"name":"pavan","age":23}
result=student.setdefault("course","fullstack")
print(result)
print(student)

student={"name":"pavan","age":23}
result=student.setdefault("adresss")
print(result)
print(student)

#set
s={17, 18, 5, 3, 20}
#methods in sets
#add()
#remove()
#discard()
s.add(20)
print(s)
s.remove(20)
print(s)
s.discard(20)
print(s)
s.discard(4)
print(s)

#union
#intersection
s1 ={1,2}
s2 ={2,3}
print(s1.intersection(s2))
print(s1|s2)
print(s1&s2)


key = {'mdl','dist','city'}
dict1=dict.fromkeys(key,'hyderabad')
print(key)

# strings 
# concatenation
# repetition 
# replace 
str1="python"
str2="programming language"
print(str1+" "+str2)
print(str1*3) 
print(str2.replace("programming","ajaysir")) 
text="ajay sir"
print(len(text))