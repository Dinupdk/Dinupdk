#Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.
#Expected Input: 5
#Expected Output: 15 (1 + 2 + 3 + 4 + 5)

n=int(input("Enter value to calculate sum of numbers from 1 to n : "))
#n=10
i=0
sum=0
while i<=n:
    sum=sum+i
    i=i+1

print(sum)