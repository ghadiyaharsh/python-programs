'''Write a Python program to count the number of strings where the string length is 2 or more        
and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2 '''

def count_strings(strings):
    # Initialize the counter
    count = 0

    # Iterate through each string in the list
    for string in strings:
        # Check the conditions: length >= 2 and first and last character are the same
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1

    return count

# Sample List
sample_list = ['abc', 'xyz', 'aba', '1221']

# Call the function and print the result
result = count_strings(sample_list)
print("Expected Result:", result)


