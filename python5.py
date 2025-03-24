#list
# marks=[20,30,40,54,60]
# print(marks)
# print(len(marks))
# print(marks[3])

# student=[20,'karan', 45 ,24]
# print(student[1])
# student[1]="dhruv"
# print(student)

no=[1,2,3,4,5,6]
# print(no[1:4])
# print(len(no))

# print(no.append(68))
# print(no)
# print(no.sort())
# print(no)
# print(no.sort(reverse=True))
# print(no)
# print(no.reverse())
# print(no)
# print(no.insert(3,9))
# print(no)

#tuple
tup=(2,3,4,5,6)
print(type(tup))

print(len(tup))
print(tup[0])
print(tup[4])
print(tup[1:3])
print(tup[ :1])
print(tup[1: ])
# tup[1]=9  #not allowed in python [only happen in list in python]
# print(tup[1])

tup=()
print(tup)
print(type(tup))

movie=('ddlj, krish, war')
print(type(movie))
print(movie)

# m1=input('enter a name of movie')
# print(m1)
# m2=input('enter a name of movie')
# print(m2)
# m3=input('enter a name of a movie')
# print(m3)

# movie=(m1,m2,m3)
# print(movie)
# print(type(movie))

list=[1,2,3,4]
copylist1=list.copy()
copylist1.reverse()
if(copylist1==copylist1.reverse()):
    print(True)
else:
    print(False)

tup=( "c" ,"d", "a" ,"a","b" ,"b","a")
print(tup.count("a"))
print(tup.count("b"))
list6=[ "c" ,"d", "a" ,"a","b" ,"b","a"]
print(list6.sort())
print(list6)

a='thirty'
b='days'
c='of'
d='python'
space=' '
sentence=a + space + b + space + c + space +  d
print(sentence)

a='thirty'
b='days'
c='of'
d='python'
sentence=(a+ "\t" +  b +"\t" +  c +"\t"+ d)
print(sentence)

p="coding"
l="for"
m="all"
sen=(p+"\t"+l+"\t"+m)
print(sen)

