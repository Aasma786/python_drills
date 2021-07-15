def is_prime(m):
    i=2
    f=0
    while(i<m):
        if(m%i==0):
            f=1
        i=i+1
    if(f==0):
        print(m, "is a prime number")
    else:
        print(m, "is not a prime number")
    """
    Check whether a number is prime or not
    """


def n_digit_primes(digit,n):
    my_list=[]
    while(digit<=n):
        j=1
        f=0
        while(j<=digit):
            if(digit%j==0):
                f=f+1
            j=j+1
        if(f==2):
            my_list.append(digit)
        digit=digit+1
    print("prime number between 2 to",n,":")
    print(my_list)
    """
    Return a list of `n_digit` primes using the `is_prime` function.

    Set the default value of the `digit` argument to 2
    """
m=int(input("Enter any number to check whether it's a prime or not:"))
is_prime(m)
n=int(input("Enter the value of n:"))
n_digit_primes(2,n)

