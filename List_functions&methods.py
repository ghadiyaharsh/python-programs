#write a program to implement functions and methods of List

#functions

list1=[23.12,65,231]

print(len(list1))
print(max(list1))
print(min(list1))
print(sum(list1))
print(sorted(list1))


#methods

list_1=["arjun","ved","krish",23,678]
list_1.remove("krish")        
print(list_1)

list2=[23,54,67,87,"kavy"] 
list2.remove(54)       #remove specific elemets of the list
print(list2)

list2.append(45)      #add one element at the end 
print(list2)    

list2.insert(2,"rajdeep")
print(list2)

list2.pop(2)
print(list2)