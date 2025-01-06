#Write a program to find the prime number in a specific range using filter


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Specify the range
start_range = 1
end_range = 50

# Create a list of numbers in the range
numbers = list(range(start_range, end_range + 1))

# Use filter to find prime numbers in the range
prime_numbers = list(filter(is_prime, numbers))

# Output the result
print("Prime numbers between", start_range, "and", end_range, "are:", prime_numbers)
