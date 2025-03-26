#revision
print('hello world')
name='leisha'
print(name)
a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a//b)
print(a/b)
print(a!=b)
print(a==b)
print(a**b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

print(type(a))
print(type(name))

#this is acomment
#ctrl+/=comment out

v1=5
v2=8
print("and operator:" ,v1 and v2)
print("or operator:" , v1 or v2)
print(len(name))
print(name.index)

c=float(v2)

# batch=input("enter your batch year;")
# print(batch)
# branch=input('in what branch u are:')
# print(branch)

space=" "
last="choudhary"
print(name + space + last)
print(name[1])

print(name[1:])
print(last[4:6])
print(last[-1:-5])

print(last.endswith("er"))
print(name.replace("sha","shi"))
print(name.capitalize())
print(last.find("dh"))
print(last.count("a"))

#conditional
a=5
if( a==7):
    print("yes")
else:
    print("no")

w=4
e=5
u=5
if(w==4):
    
 if(e==u):
    print("done")

    #area
# side=int(input("enter a no"))
# print(side)
# area=side*side
# print(area)

marks=[87,88,90,91,94,90,78]
print(type(marks))
print(len(marks))
print(marks[5])
marks[4]=100
print(marks)
print(marks[ :5])
print(marks[5:6])
print(marks.append(80))
print(marks)

print(marks.sort())
print(marks)
print(marks.sort(reverse=True))
print(marks)


greet="good morning"
print(greet[: :-1])
print(greet[0:5:3])

#tuple
tup=(20,35,40,50)
print(tup[0])
print(tup[3])
print(tup[1:3])

INFO={
   "name ":"leisha",
   "age": "20",
   "class" :"cse ds",
}
print(INFO)
print(type(INFO))
