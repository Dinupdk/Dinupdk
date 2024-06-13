'''
1. Example: Get the first character of the sentence.
Input: "The sun is shining."
Output: "T"

a="The sun is shining."
print(a[0])
'''
'''
2. Example: Get the last character of the sentence.
Input: "She sells seashells by the seashore."
Output: "."

a="She sells seashells by the seashore."
print(a[-1])
'''
'''
3. Example: Get the character at index 3.
Input: "I love Python!"
Output: "o"
a="I love Python!"
print(a[3])
'''

'''
4. Example: Get the second last character of the sentence.
Input: "Life is beautiful."
Output: "l"
a="Life is beautiful."
print(a[-2])
'''
'''
5. Example: Get a substring from index 7 to index 14 (exclusive).
Input: "Welcome to Python programming."
Output: " to Pyt"
a="Welcome to Python programming."
print(a[7:14])
'''
'''
6. Example: Get a substring from index -9 to -3.
Input: "The future is bright."
Output: "s brig"
a="The future is bright."
print(a[-9:-3])
'''


'''
7. Example: Get the first six characters of the sentence.
Input: "Good things take time."
Output: "Good t"
a= "Good things take time."
#print(a[::6]) #printing one char drop 5characters
print(a[0:6])
'''

'''
8. Example: Reverse the sentence using slicing.
Input: "Python is awesome!"
Output: "!emosewa si nohtyP"
a="Python is awesome!"
print(a[::2])#[::-1]reverse the sentence],[::1]normal,[::n]jumping char
'''
'''
9. Example: Get the length of the sentence using indexing.
Input: "Coding is fun!"
Output: 14
'''
a="Coding is fun!"
print(len(a))
