# Question 4: Nested functions and variable scopes
# Write a function called outer_function that has a local variable outer_variable with the value "I'm outer". 
# Inside the outer_function,define another function called inner_function 
# that has a local variable inner_variable with the value "I'm inner". 
# The inner_function should print both the outer_variable and inner_variable. 
# Then, call the outer_function and print the outer_variable outside the function.

'''
def outer_function():
    if __name__=='__main__':
        outer_variable="I am outer"
        return outer_variable
    inner_function()

    def inner_function():
        inner_variable='I am inner'
        print(inner_variable)

print(outer_function())
# print(inner_function()) =>Error
outer=outer_function()
#print(outer.inner_function())
'''
def outer_function():
    outer_variable = "I'm outer"
    
    def inner_function():
        inner_variable = "I'm inner"
        print(outer_variable)  # Accessing outer_variable from the outer function
        print(inner_variable)
    
    inner_function()
    
# Call the outer_function
outer_function()

# Attempt to print outer_variable outside the function (this will raise an error)
try:
    print(outer_variable)
except NameError as e:
    print(f"Error: {e}")
