#3. Write a Python function that takes a string as input and checks 
# if it contains the letter 'o'. If it does, print "Found 'o'" and
#  use the `break` statement to stop searching.
#Input: "Hello, World!"

s="Hello, World!"
for i in s:
    if i=='o' or i=='O':
        print('found "O"')
        break
    print(i)