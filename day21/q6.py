#**Question 6: Adding multiple elements to a set**
#Expected Input: Set: {1, 2, 3}, Elements to add: {4, 5}
#Expected Output: Set: {1, 2, 3, 4, 5}
s1={1, 2, 3}
s2={4,5}
s1.update(s2)
print(s1)