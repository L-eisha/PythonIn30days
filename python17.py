# FULL REVISION TILL NOW
print("HELLO WORLD" ,"LEISHA HERE!")
# operations and type
a1=24
a2=89
print(a1+a2)
print(a1-a2)
print(a1*a2)
print(a1**a2)
print(a1!=a2)
print(a1==a2)
print(a1>=a2)
print(a1<a2)
print(type(a2))
a1=a1+1
print(a1)
a2=str(a2)
print(type(a2))
# HELLO WORLD LEISHA HERE!
# 113
# -65
# 2136
# 689922823738748289569678722457303368025854318182334628509535763762267553432378023689439264783448453642383249654228109492224
# True
# False
# False
# True
# <class 'int'>
# 25
# <class 'str'>


# input
# 6
# 36
# r=int(input("enter radius"))
# pi=3.14
# area=int(pi*(r*r ))
# print(area)

person = {
    'first_name':'Leisha',
    'last_name':'Choudhary',
    'age':19,
    'country':'india',
    'skills':[ 'Data Science', 'C', 'Python'],
    'address':{
        'street':'Mars street',
        'zipcode':'****'
    }
    }
print(person)
# {'first_name': 'Leisha', 'last_name': 'Choudhary', 'age': 19, 'country': 'india',
#  skills': ['Data Science', 'C', 'Python'], 'address': {'street': 'Mars street', 'zipcode': '****'}}
str="hello everyone "
ch=str[4]
print(ch)
print(str[3:6])
print(str[2:5:8])
print(str.endswith("iam"))
print(str.capitalize())
print(str.replace("everyone" , "leisha"))
print(str.find("i"))
print(str.find("o"))
# o
# lo
# l
# False
# Hello everyone
# hello leisha
# -1
# 4


marks=[85,95,90,91,72,86]
print(marks[2:5])
print(marks.append(81))
print(marks.sort())
print(marks.sort(reverse=True))
print(marks.insert(3,95))
# [90, 91, 72]
# None
# None
# None
# None
print(marks.append(81))
print(marks)
print(marks.sort())
print(marks)
print(marks.sort(reverse=True))
print(marks)
print(marks.insert(3,95))
print(marks)
# None
# [95, 91, 90, 95, 86, 85, 81, 72, 81]
# None
# [72, 81, 81, 85, 86, 90, 91, 95, 95]
# None
# [95, 95, 91, 90, 86, 85, 81, 81, 72]
# None
# [95, 95, 91, 95, 90, 86, 85, 81, 81, 72]


# reversing a string
print(str[: : -1])
# enoyreve olleh

height=[168,176,145,159,165,182]
print(marks.extend(height))
print(height)
print(marks)
# None
# [168, 176, 145, 159, 165, 182]
# [95, 95, 91, 95, 90, 86, 85, 81, 81, 72, 168, 176, 145, 159, 165, 182]

