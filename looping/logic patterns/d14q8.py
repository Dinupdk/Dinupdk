#Create a nested loop to find and print prime numbers from 2 to 20.

# Function to check if a number is prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nested loop to find and print prime numbers from 2 to 20
k=int(input('Enter value for get prime numbers from 2 to your number :'))
print("Prime numbers from 2 to 20:")
for num in range(2, k+1):
    if is_prime(num):
        print(num)


