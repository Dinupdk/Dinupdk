'''
Write a program that takes a character as input and prints "Vowel" if it's a vowel (a, e, i, o, u),
and "Consonant" otherwise.
'''
a=input("Enter one character :")    # 

if a=='a' or a=='e' or a=='i' or a=='o' or a=='u' or  a=='A' or a=='E' or a=='I' or a=='O' or a=='U':
    print(a,"is Vowel")
else:
    print(a,"is Consonant")

'''
a=input("Enter one character :")

if a=='a' or a=='A':
    print(a,"is Vowel")
elif a=='e' or a=='E' :
    print(a,"is Vowel")
elif a=='i' or a=='I' :
    print(a,"is Vowel")
elif a=='o' or a=='O':
    print(a,"is Vowel")
elif a=='u' or a=='U' :
    print(a,"is Vowel")
else:
    print(a,"is Consonant")
    '''

'''

a=str(input('enter one character :'))
b=a.upper()
if  b=='A' or b=='E' or b=='I'  or b=='O'  or b=='U':
    print(a,'is Vowel')
else:
    print(a,'is Consonant')

'''