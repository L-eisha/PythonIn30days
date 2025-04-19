#loop 
print("restart python again")
i=1
while i <= 20:
    if(i%2!=0):
        i=i+1
        continue
    print(i)
    i=i+1
    

#for loops= sequential traversal
list=[1,2,3,4]
for el in list:
    print(el)


#for loop with else
list=[1,2,3,4]
for el in list:
    print(el)
else:
    print("end")