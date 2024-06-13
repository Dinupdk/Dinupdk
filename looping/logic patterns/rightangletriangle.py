# Example: Print a right-angled triangle pattern using nested loops
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Move to the next line after each row
