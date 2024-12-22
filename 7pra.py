with open("practice.txt","r") as f:
    data = f.read()
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")



        # NUMPY LIBRARY

import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print(type(arr1))
print(arr1.shape)
print("numbe of dimension of arr1 is :-",arr1.ndim)
print(arr)

print(arr[0])     #acces 1-D array elements
print(arr[2]+arr[3])

print(arr1[0,1]) # access 2-D array elements
print(arr1[1,-1])

print(arr[1:3])     #slicing of array
print(arr[1:])
print(arr[0:4:2])
print(arr[:4])
print(arr[-2:-1])
print(arr1[1,1:3])   #2-D array sllicing


print(arr.dtype) #check the dtype 




# dtype in numpy 

"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
