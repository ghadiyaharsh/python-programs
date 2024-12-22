marks1=92.3
marks2=93.2
marks3=94.7
marks4=95.5
marks5=96.4


marks=[92.3,93.2,94.7,95.5,96.4]    #list in python like as array
print(marks)
print(type(marks))
print(marks[0])       #index of marks
print(marks[2])
print(len(marks))


student=["karan",85,"harsh","Rajkot"]      #allowed different data type over c and c++.

#string - inmutable (no change)
#list  - mutable (change)
print(student)
student[0]="karan"
print(student[0])


#list slicing
student1=["karan",85,"harsh","Rajkot"]      
print(student1[2:3])
print(student1[0:2])
print(student1[-1:-3])


#list method(function)
list=[1,3,2,4]
list.append(5)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.insert(0,8)     #first is index and second is no. which is replce into given index
print(list)


list1=[1,3,2,4,5,2,3,1]
list1.remove(1)  #removes first occurrence of element
print(list1)
list.pop(2) #removes element at index
print(list1)



#tuples

tup=()
print(tup)
print(type(tup))


tup1=(1,)  #when one no. 
print(tup1)

tup2=(9,1,3,2,4)     #tuple slicing
print(tup2[2:4])

#tuple method
tup2.index(1) #return index of first occurrence
print(tup2)
tup2.count(3)
print(tup2)




#pr-1
m1=input("enter first movie :-")
m2=input("enter second movie :-")
m3=input("enter third movie :-")

print("movie1 :-",m1)
print("movie2 :-",m2)
print("movie3 :-",m3)



list=[m1,m2,m3]
print(list)



#pr-2
tup4=("c","d","a","a","b","b")
print(tup4.count("a"))

