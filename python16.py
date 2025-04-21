#loop 
print("restart python again")
i=1
while i <= 20:
    if(i%2!=0):
        i=i+1
        continue
    print(i)
    i=i+1
#     2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

#for loops= sequential traversal
list=[1,2,3,4]
for el in list:
    print(el)
# 1
# 2
# 3
# 4

#for loop with else
list=[1,2,3,4]
for el in list:
    print(el)
else:
    print("end")

# 1
# 2
# 3
# 4
# end
name=["a","b","c"]
for el in name:
    print(el)
#     a
# b
# c

str="leisha choudhary"
for char in str:
    print(char)
# l
# e
# i
# s
# h
# a

# c
# h
# o
# u
# d
# h
# a
# r
# y

st2="what is this"
for char in  st2:
    if (char=="i"):
        print("i found")
        break
    print(char)
else:
    print("end")
# w
# h
# a
# t

# i found

no=[1,4,9,16,25,36,49,64,81,100]
for el in no:
    print(no)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

no=[1,4,9,16,25,36,49,64,81,100]
for el in no:
    print(el)
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

tup=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for el in tup:
    if(el==x):
        print("no found at index",idx)
    idx+=1
# no found at index 6
# no found at index 10
tup=(1,4,9,16,25,36,49,64,81,100,49)
x=49
idx=0
for el in tup:
    if(el==x):
        print("no found at index",idx)
        break
    idx+=1
    # no found at index 6

# RANGE {return a sequence of no. starting from 0}
numbers=(1,2,3,5,6,89,0,98)
for el in range(5):
 print(el)
#  0
# 1
# 2
# 3
# 4


for el in range(1,4):
 print(el)
# 1
# 2
# 3

for el in range(1,4):
 print(el)