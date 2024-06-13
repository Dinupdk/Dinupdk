'''
Write a program that takes a year as input and prints "Leap Year" if it's a leap year, and "Not a Leap Year" otherwise.
'''
a=int(input('Enter year:'))
b=a%4
if b==0:
    print(a,'is leap year')
else :
    print(a,'is not leap year')