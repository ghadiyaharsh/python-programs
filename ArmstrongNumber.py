# program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num  # Make a copy of the original number
while temp > 0:  # Loop until all digits are processed
   digit = temp % 10  # Get the last digit
   sum += digit ** 3  # Cube it and add to sum
   temp //= 10  # Remove the last digit

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
