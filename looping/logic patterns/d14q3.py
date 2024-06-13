#Write a nested loop to print a right-angled triangle of numbers in ascending order.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''for i in range(1,6):
    for j in i:
        print(j) '''
# Function to print a right-angled triangle of numbers in ascending order
'''def print_triangle(rows):
    num = 1  # Starting number
    for i in range(1, rows + 1):  # Outer loop for each row
        for j in range(1, i + 1):  # Inner loop for numbers in each row
            print(num, end=' ')  # Print the number
            num += 1  # Increment the number
        print()  # Move to the next line after each row

# Example usage
rows = 5
print_triangle(rows)'''
# Function to print a right-angled triangle of numbers in ascending order
'''def print_triangle(rows):
    for i in range(1, rows + 1):  # Outer loop for each row
        for j in range(1, i + 1):  # Inner loop for numbers in each row
            print(j, end=' ')  # Print the number
        print()  # Move to the next line after each row

# Example usage
rows = 5
print_triangle(rows)
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
