#!/usr/bin/python

def fib(n=5):
    '''They say that it's a good practice for this is called docstring

    And the first line should be started with a Capital
    Then the second line should be an empty one
    You can use fib.__doc__ to print this docstring
    '''
    a, b, i, result = 0, 1, 0, []
    for i in range(n):
        a, b = b, a + b
        result.append(b)
    return result

#check prime number
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    else:
        return 1

if __name__ == '__main__' :
    print "Do not run this script alone"