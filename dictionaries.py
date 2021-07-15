def word_count(s):
    a=[]
    a= s.split()
    count=len(a)
    print(count)
    """
f    Find the number of occurrences of each word
    in a string(Don't consider punctuation characters)
    """
    pass


def dict_items(d):
    print("dictionary items:")
    for i in d:
        print(i,":",d[i])
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    """
    pass


def dict_items_sorted(d):
    a=sorted(d.items(),key=lambda x: x[1])
    print("sorted dictionary items:")
    for i in a:
        print(i[0],':',i[1])
    """
    Return a list of all the items - (key, value) pair tuples - of the dictionary, `d`
    sorted by `d`'s keys
    """
    pass
word_count("Don't consider punctuation characters")
dict_items({'1':'one','4':'four','3': 'three','2':'two'})
dict_items_sorted({ 'three':'3','four':'4','two':'2','one':'1'})
