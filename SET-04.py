#1 Write a python program which covers all the methods (functions) of list. 

list1=[1,2,3,4,5,67,234]

#methods
list1.append(6)  #add last element in list
print(list1)   #[1, 2, 3, 4, 5, 67, 234, 6]

list1.insert(1,44) #add elelemet at specific index
print(list1)     #[1, 44, 2, 3, 4, 5, 67, 234, 6] 

list1.remove(234) #remove element from list 
print(list1)    #[1, 44, 2, 3, 4, 5, 67, 6]

list1.pop() #remove last element from list
print(list1)    #[1, 44, 2, 3, 4, 5, 67]

list1.pop(3) #remove element from specific index
print(list1)    #[1, 44, 2, 4, 5, 67]

list1.clear() #clear all elemets from list
print(list1)     #[]

list1.extend([76,89,34,234,87,567])
print(list1)    #[76, 89, 34, 234, 87, 567]

#2 Write a Python program to append a list to the second list.

list1=[1,2,3,4,5]
list2=[9,8,7,6,5]
list2.append(list1)
print(list2)


