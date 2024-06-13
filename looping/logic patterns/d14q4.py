'''
Create a nested loop that prints a hollow square pattern of stars (asterisks).
output
*****
*   *
*   *
*   *
*****'''
# Function to print a hollow square pattern of stars
def print_hollow_square(size):
    for i in range(size):  # Outer loop for each row
        for j in range(size):  # Inner loop for each column
            # Print '*' at the borders or spaces otherwise
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()  # Move to the next line after each row

# Example usage
size = 5
print_hollow_square(size)
