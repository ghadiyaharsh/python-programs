#write a pyhton program to implement the given list is a palindrome or not


def palindrome(x):
    reversed_list = list(reversed(x))
    if x == reversed_list:
        print("The given list is a palindrome.")
    else:
        print("The given list is not a palindrome.")

list1 = [1, 4, 2]
palindrome(list1)

#if we want to take a list from use so we can take list1=int(input("Enter a List"))
