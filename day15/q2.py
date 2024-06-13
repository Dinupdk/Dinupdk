#Given a list of numbers [1, 2, 3, 4, 5], 
#use a for loop to print the elements one by one.
#However, if the element is 3, skip it using the continue statement.

l=[1,2,3,4,5]
for i in l:
    if i==3:
        continue
    print(i)