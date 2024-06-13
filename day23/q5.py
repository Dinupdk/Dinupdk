#Problem 5: Function with default parameter value
#Write a function called greet_user that takes an optional name parameter with a default value of "Guest".
#The function should return a greeting message with the provided name or "Guest" if no name is provided.

def greet_user(name="Guest"):
    return "hii"+name#f"Hello, {name}!"

# Example usage
print(greet_user("Alice"))  # Output: Hello, Alice!
print(greet_user())         # Output: Hello, Guest!