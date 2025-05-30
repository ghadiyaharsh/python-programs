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
list2.extend(list1)
print(list2)




#3 write a pyhton program to check the given list is palindrome or not.
list1=[1,2,3,4,5,4,3,2,1]
if list1==list1[::-1]:
    print("list is palindrome")
else:
    print("list is not palindrome")

    
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
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_up_to_n(N):
    primes = []
    for num in range(2, N + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input: N
N = int(input("Enter a number: "))

# Print the list of prime numbers up to N
prime_numbers = print_primes_up_to_n(N)
print(f"Prime numbers up to {N}: {prime_numbers}")


#6 Write a python program to print the list of even numbers using loop and clauses.

def is_even(num):
    return num % 2 == 0

def print_even_numbers_up_to_n(N):
    even_numbers = []
    
    for num in range(1, N + 1):  # Loop from 1 to N
        if is_even(num):
            even_numbers.append(num)
    return even_numbers
    
        
#7 Write a python program to print the list of odd numbers using loop and clauses.

def is_odd(num):
    return num % 2 != 0
def print_odd_numbers_up_to_n(N):
    odd_numbers = []
    
    for num in range(1, N + 1):  # Loop from 1 to N
        if is_odd(num):
            odd_numbers.append(num)
    return odd_numbers


is_odd(12)