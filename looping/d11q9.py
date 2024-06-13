#Write a while loop that reads numbers from the user until they enter the number 0.
# Then, it prints the sum of all the entered numbers.
#Expected Input: 3, 5, 2, 0
#Expected Output: 10 (3 + 5 + 2)
sum=0
i=int(input('Enter values :'))
while i>0 or i<0:
    sum=sum+i
    i=int(input('Enter values :'))
print('Sum=',sum)
