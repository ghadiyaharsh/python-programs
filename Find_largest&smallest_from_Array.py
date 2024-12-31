print("hello this program is about find largest and smallest number from Array")

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