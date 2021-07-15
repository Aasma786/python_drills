def sum_items_in_list(x):
    sum1=0
    for i in x:
        sum1=sum1+i
    print("Sum of list [15,12,3,6,4,3] is:" ,sum1)
    pass


def list_length(x):
    length=len(x)
    print("Length of list is:",length)
    pass


def last_three_items(x):
    n=3
    res=x[-n:]
    print("Last three items of list:",res)
    pass


def first_three_items(x):
    n=3
    res=x[:n]
    print("First three items of list:",res)
    pass


def sort_list(x):
    x.sort()
    print("Sorted List:",x)
    pass


def append_item(x, item):
    x.append(item)
    print("New list added:",x)
    pass


def remove_last_item(x):
    del x[-1]
    print("After removing last element of the list:",x)
    pass


def count_occurrences(x,item1):
    count=0
    for i in x:
        if(i==item1):
            count=count+1
    print(item1, "has occurred",count,"times")
    pass

def is_item_present_in_list(x, item2):
    if item2 in x:
        print(item2,"is present in list")
    else:
        print("No such item in list")
    pass


def append_all_items_of_y_to_x(x, y):
    x[len(x):]=y
    print("After appending all item of y in x:",x)
    """
    x and y are lists
    """
    pass


def list_copy(x):
    y=x.copy()
    print("copied list:",y)
    """
    Create a shallow copy of x
    """
x=[15,12,3,6,4,3]
item=10
item1=3
sum_items_in_list(x)
list_length(x)
last_three_items(x)
first_three_items(x)
sort_list(x)
append_item(x,item)
remove_last_item(x)
count_occurrences(x,item1)
item2=int(input("Enter the number you want to search in list:"))
is_item_present_in_list(x, item2)
y=[5,11]
append_all_items_of_y_to_x(x, y)
list_copy(x)
