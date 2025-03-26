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

_______________________________________________________________________________________________________________________

#2 Write a Python program to append a list to the second list.

list1=[1,2,3,4,5]
list2=[9,8,7,6,5]
list2.append(list1)
print(list2)
list2.extend(list1)
print(list2)

________________________________________________________________________________________________________________________


#3 write a pyhton program to check the given list is palindrome or not.
list1=[1,2,3,4,5,4,3,2,1]
if list1==list1[::-1]:
    print("list is palindrome")
else:
    print("list is not palindrome")

_________________________________________________________________________________________________________________________
    
# 4 Write a python program to store strings in a list and then print them.
list1=["hi","raj","jay","man"]
print(list1)
print(type(list1))

#5 write a python program to print a list of palindrome number using loop by N numbers
n=int(input("enter the number:"))
list1=[]
for i in range(1,n+1):
    if str(i)==str(i)[::-1]:
        list1.append(i)
        print(list1)

#5 write a python program to print a list of prime numbers upto N using loop and clauses.
x = range(5)
print(x)
for i in x:
    if i%2 == 0:
        break
    else:
        print("prime number ",i)
        

        
