'''  Flatten a nested list structure. 
Example: if list1 = [1, [2, 3], [4, 5, 6,  ] ] then try to convert it in 1-dimensional [1, 2, 3, 4, 5, 6, 7]'''


nested_list = [1, [2, 3], [4, 5, 6]]

flattened_list = [
    item
    for sublist in nested_list  # Iterate through main list
    for item in (sublist if isinstance(sublist, list) else [sublist])  # Check if sublist is a list
]
print(flattened_list)  #[1,2,3,4,5,6]

