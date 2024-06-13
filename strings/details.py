#len(): Returns the length of the string.
string = "Hello, World!"
length = len(string)
print('length of the string:',length)  # Output: 13

#lower(): Converts all characters in the string to lowercase.
string = "Hello, World!"
lower_case = string.lower()
print('string lowercase:',lower_case)  # Output: hello, world!

#upper(): Converts all characters in the string to uppercase.
string = "Hello, World!"
upper_case = string.upper()
print('stringuppercase:',upper_case)  # Output: HELLO, WORLD!

#strip(): Removes leading and trailing whitespaces from the string.
string = "   Hello, World!   "
stripped_string = string.strip()
print('remove front and back unwanted spaces of the string:',stripped_string)  # Output: "Hello, World!"

#replace(): Replaces occurrences of a substring with another substring.
string = "Hello, World!"
new_string = string.replace("Hello", "Hi")
print('replace the hello to hi:',new_string)  # Output: "Hi, World!"

# split(): Splits the string into a list of substrings based on a delimiter.
string = "apple,orange,banana"
fruits = string.split(",")
print('split and convert into list:',fruits)  # Output: ['apple', 'orange', 'banana']





#startswith(): Checks if the string starts with a specific prefix.
string = "Hello, World!"
result = string.startswith("Hello")
print('string start with Hello :',result)  # Output: True

# endswith(): Checks if the string ends with a specific suffix.
string = "Hello, World!"
result = string.endswith("World!")
print('string ends with World!',result)  # Output: True

# count(): Returns the number of occurrences of a substring in the string.
string = "Hello, World!"
count = string.count("l")
print('number of "l"s present in string:',count)  # Output: 3

# find(): Returns the index of the first occurrence of a substring. If not found, returns -1.
string = "Hello, World!"
index = string.find("o")
print('find the index of "o"',index)  # Output: 4

# isdigit(): Checks if all characters in the string are digits.
string = "12345"
result = string.isdigit()
print('value is string or not :',result)  # Output: True

# isdigit(): Checks if all characters in the string are digits. 
string = "Hello"
result = string.isalpha()
print('is variable contains string ',result)  # Output: True

# 
# #