#sets
# syntax
st = set()
print(st)
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
name={"riya","kashish","manya"}
print(len(name))
print(type(name))
# syntax for checking if a 
st = {'item1', 'item2', 'item3', 'item4'}
print('item1' in st )
print(st.add('item5'))
print(st)
#another method
st.update('item6','item7')
print(st)#{'item1', 'item4', 'i', 't', 'item3', '7', 'item5', 'm', 'e', 'item2', '6'} output

# syntax for remove
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.remove()  
# print(fruits.remove[2])
#error.......

#The pop() methods remove a random item from a list and it returns the removed item.
print(st.pop())
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
print(st1.intersection(st2))

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1)
print(st2.issubset(st1)) # True
st1.issuperset(st2)
print(st1.issuperset(st2)) # True

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) 
print(st2.difference(st1) )# set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
print(st1.difference(st2))

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1)
print(st2.isdisjoint(st1)) # False


#QUESTIONS
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
print(len(it_companies))
#2
it_companies.add('twitter')
print(it_companies.add('twitter'))
print(it_companies)

it_companies.update('plunge','boat')
print(it_companies.update('plunge','boat'))
print(it_companies)
#{'Oracle', 'e', 'twitter', 'Amazon', 'a', 'Google', 'Facebook', 'Microsoft', 'Apple', 'IBM', 'n', 'p', 'u', 'l', 't', 'b', 'g', 'o'}
it_companies.add("asus")
print(it_companies.add("asus"))
print(it_companies)

print(it_companies.remove('IBM'))
print(it_companies)
#level2 exercise
st3=A.union( B)
print(st3)
print(A.intersection(B))
print(A.issubset(B) )
print(A.intersection(B))
print(B.intersection(A))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A
# print(A)
# del B
# print(B)

#LEVEL3
age=set(age)
print(age)
print(len(age))

