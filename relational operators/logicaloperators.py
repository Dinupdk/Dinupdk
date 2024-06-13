#1. `and`: Returns True if both operands are True.
#2. `or`: Returns True if at least one of the operands is True.
#3. `not`: Returns the opposite boolean value of the operand.
'''
1. Example: "and" operator with two True conditions
Input: (10 > 5) and ("apple" == "apple")
Output: True
2. Example: "and" operator with one False condition
Input: (3 < 2) and ("banana" == "orange")
Output: False
3. Example: "and" operator with one True and one False condition
Input: (5 >= 3) and (10 != 10)
Output: False
4. Example: "or" operator with two True conditions
Input: ("car" == "car") or (7 < 9)
Output: True
5. Example: "or" operator with one False condition
Input: ("dog" == "cat") or (6 < 10)
Output: True

6. Example: "or" operator with both False conditions
Input: (2 == 3) or (8 > 15)
Output: False
7. Example: "not" operator with True condition
Input: not (4 <= 3)
Output: True
8. Example: "not" operator with False condition
Input: not ("orange" == "orange")
Output: False
9. Example: "not" operator with "and" and "or"
Input: not ((5 > 3) and ("apple" != "banana"))
Output: False
10. Example: "and" and "not" operators combined
Input: (10 > 5) and not (3 < 2)
Output: True
11. Example: "or" and "not" operators combined
Input: ("cat" == "cat") or not (6 > 10)
Output: True
12. Example: Using parentheses for grouping expressions
Input: ((5 >= 3) and (10 != 10)) or (8 > 15)
Output: False
13. Example: Combining multiple "and" operators
Input: (2 < 5) and (10 == 10) and ("hello" != "world")
Output: True
14. Example: Combining multiple "or" operators
Input: (7 < 3) or (5 >= 5) or ("apple" == "apple")
Output: True
15. Example: Using "not" operator with an expression
Input: not (10 > 5 and "car" != "car")
Output: True
16. Example: Using "not" operator with "or" and "and"
Input: not (5 > 3 or "dog" == "cat" and 7 < 5)
Output: False
17. Example: Combining "and" and "or" operators
Input: (5 > 3 and "apple" != "banana") or (8 == 8 or 6 < 10)
Output: True
18. Example: Combining "or" and "not" operators
Input: ("apple" == "banana" or not (6 > 10))
Output: True
19. Example: Complex combination of "and", "or", and "not"
Input: not (2 < 5 and (7 > 3 or "hello" == "world"))
Output: False
20. Example: Nested use of "and", "or", and "not" operators
Input: (not (5 > 3) and (10 != 10 or "car" == "car"))
Output: False'''

