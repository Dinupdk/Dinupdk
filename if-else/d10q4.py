#Assign a grade to a given percentage, considering the following grade scale:
#  A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).

a=int(input('Enter your marks :'))

if 90<=a<=100 :
    print('Grade : A')
elif 90>a>=80:
    print('Grade :B')
elif 80>a>=70:
    print('Grade :C')
elif 70>a>=60:
    print('Grade :B')
elif 60>a>=0:
    print('Fail')
elif a>100 or a<0:
    print('marks are incorrect')
else:
    print('error')