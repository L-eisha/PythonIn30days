#conditionals
#if

a=6
if(a>4):
    print(True)
else:
    print(False) #True

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')#A is a positive number

# syntax
if ():
    print()
elif ():
    print()
else:
    print()

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
#A is zero

#nested condition
    a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
#A is zero
# condition with and
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')#A is zero

r=12
if r>7 or r==7 :
    print('i am best')
elif r==10 or r/2==0 :
    print("hello world")
else:
    print("welcome")
#i am best

#questions
age=int(input("Enter your age:",) )
if age>18:
    print("old enough to drive")
else:
    print(' u need 3 more years to learn ')
# Enter your age:15
#  u need 3 more years to learn

AGE=int(input("enter your age 1"))
print(AGE)
A2=int(input("enter age A2"))
print(A2)
if AGE>A2:
    print("u r old")
else:
    print("hello young person")
# # enter your age 130
# # 30
# # # enter age A237
# # # 37
# # # hello young person

# # a=int(input("enter a value a"))
# # print(a)
# # b=int(input("enter b"))
# # print(b)
# # if (a > b):
# #     print(a)
# # else:
# #     print (b)
# # #enter a value a6
# # # 6
# # # enter b4
# # # 4
# # # 6

score = int(input("Enter a value: "))

if 80 <= score <= 100:
    print("Grade A")
elif 70 <= score <= 79:
    print("Grade B")
elif 60 <= score <= 69:
    print("Grade C")
elif 50 <= score <= 59:
    print("Grade D")
elif 0 <= score <= 49:
    print("Grade F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")

month=input("enter a month")
