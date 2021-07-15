"""
Implement the below file operations.
Close the file after each operation.
"""


def read_file():
    file1=open("D:/Aasma/FreeCodeChamp/python_drills/me1.txt","r")
    content=file1.read();
    print(content)
    file1.close()
    pass


def write_to_file():
    file2=open("D:/Aasma/FreeCodeChamp/python_drills/me2.txt","w")
    file2.write("Python is the modern day language.It makes things so simple.It is the fastest-growing programming language.")
    file2.close()
    pass


def append_to_file():
    file3=open("D:/Aasma/FreeCodeChamp/python_drills/me3.txt","a")
    file3.write("has an easy syntax and user-friendly interaction.")
    file3.close()
    pass


def numbers_and_squares(n):
    sq=0
    for i in range(1,n+1):
        sq=i*i
        print(i,sq)
    """
    Save the first `n` natural numbers and their squares into a file in the csv format.

    Example file content for `n=3`:

    1,1
    2,4
    3,9
    """
    pass
read_file()
write_to_file()
append_to_file()
numbers_and_squares(3)
