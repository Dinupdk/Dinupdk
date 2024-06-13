#Question 2: Function with multiple parameters
#Write a function called calculate_sum that takes three parameters a, b, and c, and 
#returns the sum of the three numbers.
def calculate_sum(a=0,b=0,c=0,*args):  #*args accepts no.of arguments
    print('sum=',a+b+c+args)

calculate_sum(1,2,3,4)
calculate_sum(1,2,3)
calculate_sum(1,2)
calculate_sum(1)
calculate_sum()