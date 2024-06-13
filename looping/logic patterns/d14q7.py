# Function to print a right-angled triangle of stars
def print_triangle(rows):
    for i in range(1, rows + 1):  # Outer loop for each row
        for j in range(i):  # Inner loop for number of stars in each row
            print('*', end=' ')  # Print a star
        print()  # Move to the next line after each row

# Example usage
rows = 5
print_triangle(rows)
