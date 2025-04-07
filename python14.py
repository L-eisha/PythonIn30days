no=[ 1, 2, 3, 4, 5, ]
marvel=[ "hulk " , "thor" , ]
print(no)
print(type(no))

i=0
while i < len(marvel):
    print(marvel[i])
    i=i+1

no=[ 1, 2, 3, 4, 5, ]
i=0
x="thor"
while i < len(no):
    if (marvel[i]==x):
        print("found")
        i=i+1
    else:
        print("ok")
        break


count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
