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
(student.update({"n7":d"u"}))
print(student)