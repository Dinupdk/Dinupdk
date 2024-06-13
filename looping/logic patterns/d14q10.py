# Function to calculate and print the factorial of numbers from 1 to 5
def print_factorials():
    for num in range(1, 6):  # Outer loop for numbers from 1 to 5
        factorial = 1  # Initialize the factorial to 1
        for i in range(1, num + 1):  # Inner loop to calculate factorial
            factorial *= i  # Multiply the current value of factorial by i
        print(f"The factorial of {num} is {factorial}")  # Print the result

# Call the function
print_factorials()
