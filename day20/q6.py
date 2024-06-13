#Question: Write a function called count_vowels that takes a string text as input and returns a dictionary containing 
# the count of each vowel (a, e, i, o, u) in the text. Ignore case sensitivity.
#Expected Input: text = "Hello, World!"
#Expected Output: {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}

def count_vowels(text):
    # Initialize a dictionary with vowels and their counts set to 0
    vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convert the input text to lowercase to ignore case sensitivity
    text = text.lower()
    
    # Iterate over each character in the text
    for char in text:
        # If the character is a vowel, increment its count in the dictionary
        if char in vowels_count:
            vowels_count[char] += 1
    
    return vowels_count

# Example usage
text = "Dinesh"
result = count_vowels(text)
print(result)
