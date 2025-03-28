#dictionary
INFO={
   "name ":"leisha",
   "age": "20",
   "class" :"cse ds",
 }
# print(INFO)
# print(type(INFO))

INFO["surname"]="choudhary"
print(INFO["surname"])
INFO["name"]='sssssss'#OVERWRITE
print(INFO)

EMPTY_DICT={}
print(EMPTY_DICT)
print(type(EMPTY_DICT))

student={
    "n1":"leisha",
    "n2":"riya",
    "n2": "kashish",
    "n3":"manya",
    "subject":{

    'sci':"7", 
    'chem':"9",
    }
    
    

}
print(student)
print(type(student))
print(len(student))
print(student["subject"])

print(student.keys())
print(student.values())
print(student.items())
print(student.get("n3"))
print(student["n1"])
(student.update({"n7":"nnn"}))
print(student)


#SETS
group={1,2,3,4}
print(group)
print(type(group))
my={ }
print(type(my))
#empty set
ty=set()
print(type(ty))
print(len(ty))

print(group.add(9))
print(group)
print(group.remove(2))
print(group)
