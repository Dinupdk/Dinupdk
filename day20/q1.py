#Question: Given the initial dictionary employee as {"name": "Alice", "age": 30},
#  modify the value of the key "age" to 35.
#Expected Input: employee = {"name": "Alice", "age": 30}
#Expected Output: {"name": "Alice", "age": 35}
employee = {"name": "Alice", "age": 30}
employee.update({'age':35})
print(employee)