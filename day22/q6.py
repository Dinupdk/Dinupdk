#Question 6: Removing duplicate elements from a list using a set
#Expected Input: List: [1, 2, 2, 3, 4, 4, 5]
#Expected Output: [1, 2, 3, 4, 5]
l=[1, 2, 2, 3, 4, 4, 5]
s=set(l)
print(s)
ll=list(s)
print(ll)