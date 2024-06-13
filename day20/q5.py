#Question: Given the dictionary scores, check if the key "Alice" exists. If it exists, print the associated value;
#  otherwise, print "Key not found."
#Expected Input: scores = {"Bob": 85, "Charlie": 90, "Alice": 78}
#Expected Output: 78
scores = {"Bob": 85, "Charlie": 90, "Alice": 78}
for i in scores:
    if i=="Alice":
        print(scores[i])
    elif i!='Alice':
        print('not found')