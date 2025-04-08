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

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

    # for Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

    person = {
    'first_name':'himalya',
    'last_name':'hill'
    '',
    'age':2500,
    'country':'india',
    'is_marred':False,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out