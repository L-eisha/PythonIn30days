#tuple questions
#1
emptuple=()
print(len(emptuple))
#2
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits))
print(fruits[-3:-1])
print(fruits[-4:-1])
print(fruits[-4: ])
fruits=list(fruits)
print(list(fruits))
del fruits # invALID SYNTAX
 
 #level 1 
 #1
EMP_TUP=()
print(EMP_TUP)
print(type(EMP_TUP))
print(len(EMP_TUP))

#2 3 4 5
sisters=()
brothers=("shiv", "keshav")
sisters_bothers=sisters+brothers
print(sisters_bothers)
print(len(sisters_bothers))
mother=("jassi",) # make a tuple string cannot be add
father=("arun",)
family=sisters_bothers+mother+father
print(family)

#level 2
#1 unpack ??

vegetables=("potato", "capsicum")
ap=("milk",)
fruits = ('banana', 'orange', 'mango', 'lemon')
food_stuff_tp=fruits+vegetables+ap
print(food_stuff_tp)
food_stuff_tp=list(food_stuff_tp)
print(food_stuff_tp)
print(food_stuff_tp[2:6])
print(food_stuff_tp[0:4])
print(food_stuff_tp[4:7])

#delete nho ho raha
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"estonia"in nordic_countries
print("estonia"in nordic_countries)
print("Iceland"in nordic_countries)