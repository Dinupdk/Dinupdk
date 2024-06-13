#Question 7: Using all() and any()
#Write a Python program that takes a list of boolean values as input and checks if all values are True using the all() function. Then, check if at least one value is True using the any() function.
#Expected Output:
bool_list = [True, True, False, True]
all_true=all(bool_list)
any_true=any(bool_list)

print(all_true)  # Output: False
print(any_true)  # Output: True