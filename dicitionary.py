students = {
            "Alice": {"id": "ID0001", "age":16, "grade":"A"},
            "Bob": {"id": "ID0002", "age":27, "grade":"B"},
            "Claire": {"id": "ID0003", "age":17, "grade":"C"},
            "Dan": {"id": "ID0004", "age":19, "grade":"D"},
            "Emma":{"id": "ID0005", "age":18, "grade":"A"}
            }


#print(students["Bob"]["id"],students["Bob"]["age"])

#changing values of keys
#students["Bob"]["grade"]="A"
#print(students["Bob"])

#del a key
del students["Bob"]["age"]
#print(students["Bob"])

#print(students.popitem())
#print(students.keys())
#print(students.values())

#print(len(students))

#for k, v in students.items():
  #  print(k,v)

#indexing of dict
x=list(students.items())
print(x[1][0])
