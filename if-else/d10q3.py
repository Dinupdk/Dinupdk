#Classify a given age into four categories: baby, child, teenager, or adult.
age=int(input('Enter Age :'))

if age<=6:
    print('Baby')
elif 6<age and age<=14:
    print('Child')
elif 14<age and age<=20:
    print("teenager")
elif 20<age and age<=100:
    print('adult')
else:
    print('Enter correct age')