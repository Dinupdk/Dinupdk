#Given a list of numbers [1, 2, 3, 4, 5],
#use a for loop to double each element and print the result.]
#However, if the element is 4, use the continue statement to skip it.
l=[1, 2, 3, 4, 5]
for i in l:
    if i==4:
        continue
    print(i*2)