#Dictionaries and questions
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

empty={}
print(type(empty))
print(person)
print(type(person))
print(len(person))
print(person['address'])
person["car"]="BMW"
print(person)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

# syntax
dct = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':'value4'
    }
dct.pop('key1') # removes key1 item
print(dct)
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 
print(dct)

dct=list(dct)
print(dct)

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

#que
dog={}
dog["name"]="tom"
dog["age"]=6
dog["color"]="brown"
print(dog)

student={
    "name":"radhika",
    "age":5,
    "class":4,
    "rollno":8,
    "hobby":["writting","coding","cooking",]
}
print(len(student))
print(type(student["hobby"]))

student["hobby"]="dancing"
print(student)

keys=student.keys()
print(keys)

values=student.values()
print(values)

student=tuple(student)
print(student)

