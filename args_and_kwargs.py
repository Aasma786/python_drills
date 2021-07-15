def add3(a, b, c):
    print(sum([a,b,c]))
    return sum([a, b, c]) 


def unpacking1():
    items = [1, 2, 3]
    add3(*items)
    # Call add3 by passing unpacking items


def unpacking2():
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    add3(*kwargs)
    # Call add3 by unpacking kwargs


def call_function_using_keyword_arguments_example():
    a = 1
    b = 2
    c = 3
    add3(a,b,c)
    # Call add3 by passing a, b and c as keyword arguments


def add_n(*argv):
    return arg1+arg2+arg3
    """
    Define `add_n` so that it accepts
    any number of arguments and
    returns the sum of all the arguments
    """
    pass


def add_kwargs(a,b,**kwargs):
    if(argv.length()==0):
        sum =0
        sum=a+b
        return sum
    else:
        raise Exception("only 2 arguments can be passed")
        #raise an exception
    
    """
    Define `add_kwargs` so that it accepts a and b as keyword arguments
    and returns the sume of these arguments. 

    Ensure the function raises an exception when arguments apart from a and b
    are passed to `add_kwargs`
    """
    pass


def universal_acceptor(*argv, **kwargs):
    print('argv', argv, 'kwargs', kwargs)
    """
    Define `universal_acceptor` so that it accepts any kind of
    arguments and keyword-arguments,
    and prints the arguments and keyword-arguments.
    """
    pass

unpacking1()
call_function_using_keyword_arguments_example()

