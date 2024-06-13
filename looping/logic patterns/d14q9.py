#Write a nested loop that prints a diamond pattern of stars (asterisks).
def print_diamond(n):
    # Upper part of the diamond (including the middle row)
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()
    
    # Lower part of the diamond
    for i in range(n - 2, -1, -1):
        # Print leading spaces
        for j in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for k in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

# Example usage
print_diamond(3)
