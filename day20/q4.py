#Create a function called add_stock that takes a dictionary stock and 
# an item item_name (string) as input and adds 1 to the value of the corresponding key in the dictionary.
#  Return the modified dictionary.
#Expected Input: stock = {"apple": 10, "banana": 15}, item_name = "banana"
#Expected Output: {"apple": 10, "banana": 16}

def add_stock(item_name):
    stock = {"apple": 10, "banana": 15}
    stock.update({item_name:stock[item_name]+1})
    print(stock[item_name])
    print(stock)

add_stock("apple")