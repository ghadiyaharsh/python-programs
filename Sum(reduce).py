'''Write python program to make sum of particular range using reduce'''


from functools import reduce

# Define the range
start = 5
end = 10

# Create a list of numbers in the specified range
numbers = list(range(start, end + 1))

# Use reduce to calculate the sum
result = reduce(lambda x, y: x + y, numbers)

print(f"The sum of numbers from {start} to {end} is: {result}")




'''The reduce function in Python, from the functools module, can be used to compute the sum of elements in a specific range.
The reduce function applies a function cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.

Importing reduce: The reduce function is imported from the functools module as it's not built into Python's base namespace.

Define the range: Variables start and end specify the start and end of the range (inclusive). For example, if start = 5 and end = 10, the numbers are 5, 6, 7, 8, 9, 10.

Create a list: The range(start, end + 1) function generates a sequence from start to end. We convert it into a list for clarity: [5, 6, 7, 8, 9, 10].

Apply reduce:

The lambda function (x, y): x + y takes two arguments and returns their sum.
reduce applies this function cumulatively:
First step: 5 + 6 = 11
Second step: 11 + 7 = 18
Third step: 18 + 8 = 26
Fourth step: 26 + 9 = 35
Final step: 35 + 10 = 45
Output: The final result is printed as the sum of the numbers in the specified range.'''

