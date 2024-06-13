#Determine the type of a given number num: even or odd, 
# and whether it is positive or negative.
a= int(input('Enter a value :'))
if a>0:
    if a%2==0:
        print(a,'is postive and even number')
    else:
        print(a,'is postive and odd number')
elif a==0:
    print('ZERO')
else:
    if a%2==0:
        print(a,'is negative and even number')
    else:
        print(a,'is negative and odd number')