#Write a function called check_even_odd that takes a number parameter and 
# returns "Even" if the number is even, and "Odd" if the number is odd.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
num = 10
result = check_even_odd(num)
print(f"The number {num} is {result}.")  # Output: The number 10 is Even.

num = 11
result = check_even_odd(num)
print(f"The number {num} is {result}.")  # Output: The number 11 is Odd.
