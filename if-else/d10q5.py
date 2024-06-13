#Check if a given year is a leap year, and if it is,
#  find the number of days in February for that year.
a=int(input("Enter Year :"))

if a%4==0:
    print('Leap Year, February has 29 days')
else:
    print('normal year')