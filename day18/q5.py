#Check if the element 25 exists in the tuple: (10, 20, 30, 40, 50).
t=(10, 20, 25,30, 40, 50)
for i in t:
    if i==25:
        print(True)
        break

    print(False)