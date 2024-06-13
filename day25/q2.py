#Question 2: Keyword Arguments
#Write a function called greet that takes two keyword arguments name and age, and
#  prints a greeting message with the provided values.
def greet(name='user',age=25):
    return f'hii {name} and your age is {age}'
print(greet())
