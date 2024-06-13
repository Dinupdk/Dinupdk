#Question: Add a new key-value pair to the dictionary fruits, where the key is "orange" and the value is 3.
#Expected Input: fruits = {"apple": 5, "banana": 7}
#Expected Output: {"apple": 5, "banana": 7, "orange": 3}
fruits = {"apple": 5, "banana": 7}
fruits.update({"orange": 3}) 
fruits['mango']=3
print(fruits)