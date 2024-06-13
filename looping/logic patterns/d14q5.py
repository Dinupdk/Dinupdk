#Write a nested loop to calculate and print 
# the sum of numbers from 1 to 5 using nested iteration.
total=0
for i in range(1,6):
    for j in range(i,i+1):
        total=total+j
print(total)