#Question 6: Recursive function
#Write a recursive function called factorial that takes a positive integer n as input and returns its factorial.


def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: return n multiplied by the factorial of n-1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(3))  # Output: 6