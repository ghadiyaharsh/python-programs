info = {                      #dictionary
    "key":"value",
    "name":"harsh",
    "learning":"coding",
    "age":35,
    "is_allow":True,
    "subjects":["pyhotn","c","java"],
    "topics":("idct","set"),
}


null_dict={}

print(info)
print(type(info))
print(info["name"])
info["name"] = "harshghadiya"
print(info)

print(null_dict)




#nested dictionary
student={
    "name":"rahul kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":95,
    }
}


print(student)
print(student["subjects"]["chem"])




#method

print(list(student.keys()))
print(len(student))
print(student.values())
print(student.items())

print(student["name"])
print(student.get("name"))
#student.update({"city":"delhi"})
#print(student)


new_dict={"city":"delhi","age":16}
student.update(new_dict)
print(student)



#set   : -   each element is immutable & set is mutablle . --> list and dictonary can't allow in set 


collection = { 1,2,3,4,5}
print(collection)
print(type(collection))

collection1 = {1,2,3,3,3,"heelo","world",5,6,3,8,7}        #override sem value    
print(collection1)
print(type(collection1))
print(len(collection1))


collection2 = set()   #empty set : syntax
print(type(collection2))

# set method 

# set.add(el)  =  adds an element 
# set.remove(el) = removes the elem an 
# set.clear()  =  empties thee set
# set.pop() = removes the random value

collection3 = set()
collection3.add(1)
collection3.add(2)
collection3.add("harsh")
collection3.add((1,2,3))
print(collection3)
print(collection3.pop())



set1={1,2,3}
set2={2,3,4}

print(set1.union(set2))
print(set1)
print(set2)


print(set1.intersection(set2))





#prectice
set3={"python","java","c++","python","js","java","python","java","c++","c"}
print(len(set3))


marks={}
x=int(input("enter phy:-"))
marks.update({"phy":x})


x=int(input("enter chem:"))
marks.update({"chem":x})

print(marks)