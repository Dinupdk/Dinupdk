#Question 3: Function calling another function
#Write a function called square that takes a number x as input and returns the square of that number. 
# Then, write a function called square_and_double that takes a number x, calls the square function, 
# and returns twice the square value.

def square(num):
    s=num**2
    d=s+s
    print('square of',num,'is',s)
    print('double the square is',d)

square(5)

