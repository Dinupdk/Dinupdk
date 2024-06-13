#Question: Given the dictionary inventory, remove the key "sugar" and its associated value from the dictionary.
#Expected Input: inventory = {"apple": 10, "banana": 15, "sugar": 2}
#Expected Output: {"apple": 10, "banana": 15}
inventory = {"apple": 10, "banana": 15, "sugar": 2}
#inventory.popitem()
inventory.pop('sugar')
print(inventory)