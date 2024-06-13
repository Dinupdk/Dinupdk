# Function to print the reverse multiplication table from 1 to 5 up to 10 times each
def reverse_multiplication_table():
    for i in range(1, 11):  # Outer loop for multiplication factors (1 to 10)
        for j in range(5, 0, -1):  # Inner loop for numbers from 5 to 1
            print(j * i, end='\t')  # Print the product with a tab for spacing
        print()  # Move to the next line after each row

# Call the function
reverse_multiplication_table()
