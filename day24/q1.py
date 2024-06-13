#Question 1: Simple function with a default parameter
#Write a function called greet_user that takes an optional name parameter with a default value of "Guest".
#The function should return a greeting message with the provided name or "Guest" if no name is provided.

def greet_user(name='Guest'):
    print('wellcome',name)

greet_user()   #without parameter
greet_user('Dinesh')  #with parameter
