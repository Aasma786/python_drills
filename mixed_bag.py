import random
import os

def unique(items):
    unique_list=[]
    for i in items:
        if i not in unique_list:
            unique_list.append(i)
    for i in unique_list:
        print(i)
    """
    Return a set of unique values belonging to the `items` list
    """
    pass


def shuffle(items):
    random.shuffle(items)
    print(items)
    """
    Shuffle all items in a list
    """


def getcwd():
    cwd= os.getcwd()
    print("Current working directory: {0}".format(cwd))
    print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
    """
    Get current working directory
    """


def mkdir():
    dir=os.path.join("D:\Aasma\FreeCodeChamp\python_drills","Hello")
    if not os.path.exists(dir):
        os.mkdir(dir)
    """
    Create a directory at the current working directory
    """
items=[10,20,10,30,40,40]
unique(items)
shuffle(items)
getcwd()
mkdir()
