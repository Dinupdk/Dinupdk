#Write a function called sum_numbers that takes a variable number of arguments
# and returns the sum of all the arguments.
def sum_numbers(num):
    s=0
    for i in num:
        s=s+i
    print(s)

num=(1,2,3,4,5)
sum_numbers(num)