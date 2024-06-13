'''
Write a program that takes a grade as input (A, B, C, D, or F) and 
prints "Pass" if it's A, B, C, or D, and "Fail" if it's F.
'''
'''
print("Enter Grade value only A,B,C,D,F")
a=str(input('Enter Grade :'))
if a=='A' or a=='B' or a=='C' or a=='D':
    print('pass')
elif a=='F':
    print('Fail')
else:
    print('Enter only A,B,C,D,F')
    '''
print("Enter Grade value only A,B,C,D,F")
a=str(input('Enter Grade :'))
if a=='A' or a=='B' or a=='C' or a=='D':
    print('pass')
elif a=='F':
    print('Fail')
else:
    print('Enter only A,B,C,D,F')
print('Do you want to countinue press 1 or do you want to exit press any number except 1')
c=int(input('Enter your option :'))
if c==1:
    a=str(input('Enter Grade :'))
    if a=='A' or a=='B' or a=='C' or a=='D':
        print('pass')
    elif a=='F':
        print('Fail')
    else:
        print('Enter only A,B,C,D,F')
    continue
else:
    break
    


