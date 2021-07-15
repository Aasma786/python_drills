def integers_from_start_to_end_using_range(start, end, step):
    print(list(range(start, end, step)))

    """return a list"""
    pass


def integers_from_start_to_end_using_while(start, end, step):
    my_list=[]
    i=start
    j=end
    s=step
    while(i<=j):
        my_list.append(i)
        i=i+s
    print(my_list)

    """return a list"""
    pass


def two_digit_primes(lower,upper):
    my_list=[]
    for i in range(lower,upper+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                my_list.append(i)
    print(my_list)
    """
    Return a list of all two-digit-primes
    """
    pass
integers_from_start_to_end_using_range(10,50,5)
integers_from_start_to_end_using_while(1,20,3)
two_digit_primes(10,100)
