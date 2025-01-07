#write a program to find largest and smallest number from array

arr=[21,45,67,89,90,43]
print(arr)

largest=arr[0]
smallest=arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest number is:", largest)
print("Smallest number is:", smallest)
