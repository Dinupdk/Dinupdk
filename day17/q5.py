#5. Write a Python program that takes a list of names ["Alice", "Bob", "Charlie"]
# and checks if a given name (e.g., "Alice") is present in the list. 
#Print "Name found" if the name is in the list; otherwise, print "Name not found".
    
#Input: Names = ["Alice", "Bob", "Charlie"], Name = "Alice"
#Expected Output: "Name found"

l=["Alice", "Bob", "Charlie"]
for i in l:
    if i=='charlie':
        print(i,'is found')
        break
   
