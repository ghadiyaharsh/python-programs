# Function to eliminate  duplicates from list.


def remove_duplicates(input_list):
    return list(set(input_list))

example_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]    # Example list with duplicate values
new_list = remove_duplicates(example_list)   # Removing duplicates


print("Original List:", example_list)
print("List with eliminates  Duplicates:", new_list)


'''set(): Converts the list to a set, which automatically removes duplicate values because sets do not allow duplicates.
list(): Converts the set back to a list.'''
