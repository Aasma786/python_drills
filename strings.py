def last_3_characters(x):
    res=[]
    n=3
    res=x[-n:]
    print("Last three characters are:",res)
    pass


def first_10_characters(x):
    n=10
    res=x[:n]
    print("First ten characters are:",res)
    pass


def chars_4_through_10(x):
    n=10
    res=x[:n]
    r=res[:4]
    print("4 character from 10 characters:", r)
    pass


def str_length(x):
    l=len(x)
    print("Length of string is:",l)
    pass


def words(x):
    res=x.split()
    print("The List of words:" + str(res))
    pass


def capitalize(x):
    txt=x.capitalize()
    print(txt)
    pass


def to_uppercase(x):
    print(x.upper())
    pass
x=input("Enter the String:")
last_3_characters(x)
first_10_characters(x)
chars_4_through_10(x)
str_length(x)
words(x)
capitalize(x)
to_uppercase(x)
