#!/usr/bin/python
# This is my first python scripts
# so, as of many other programming language, let's start with hello world :D

print 'Hello World!, I said hello to you many times, lol'
my_name = 'nguyen_hoang_viet'
my_age = 24

print my_name
print my_age

print 'Python data type: string, unicode string'
print 'the last printed expression is assigned to the variable _ :'
print 'the first 5 letter in my full name: ' + my_name[:5]
print 'the last letter in my full name: ' + my_name[-1]
print 'the random letters: ' + my_name[1:3] + my_name[-9:-7]
print 'the length of my full name:'
print len(my_name)

print r'even this string  contain \n, it\'s not display as 2 line'
print 'r\' means raw, u\' means unicode, \'\'\' mean enter multiple line (with interactive interpreter)'

print 'Python data type: list'
squares = [1, 4, 9, 16, 25, 36]
print 'all squares:'
print squares[:]
print squares[:-4]

squares = squares + [49, 64, 81, 100]

print 'squares after add 4 elements'
print squares

squares.append(12**2)
print 'squares after append 12^2'
print squares

squares[:1] = [0, 1]

print 'squares after changing 1st elements'
print squares[:]

print 'Fibonacy Sequence with first 10 numbers here:'
i, a, b, seqs = 0, 0, 1, []
while i < 10:
    a, b = b, a + b
    print b,
    seqs.append(b)
    i = i + 1
print
print 'Odd numbers in 10 first elements of Fibonacy Sequence:'
for n in seqs:
    if n % 2 == 1:
        print n

print 'function range is so flexible'
print 'range(4):', range(4)
print 'range(10,2):', range(10, 2)
print 'range(-10,2):', range(-10, 2)
print 'range(1, 10, 3):', range(1, 10, 3)

pass

print '`pass` command is so interesting'

print "*" * 100
print 'Now, playing with function:'
print 'The interesting things are:'
print 'keywork arguments'
print 'arbitrary arguments: def my_f(*args)'
print 'dictionary arguments: def my_f(**dic)'
print 'unpacking arguments: my_f2(*[4, 5])'
print 'unpacking arguments: my_f2(**{"name":"viet","last":"nguyen"})'

def fib(n=5):
    ''' This is call the docstring
        so interesting, huh'''
    a, b, i, result = 0, 1, 0, []
    for i in range(n):
        a, b = b, a + b
        result.append(b)
    return result

print 'first 20 numbers in Fibonacci Sequence:', fib(20)
print 'first 5 numbers in Fibonacci Sequence:', fib()

print 'Now, playing with file:'
print 'All content of  readme.txt:'
file_handle = open('./read_me.txt', 'r');
for line in file_handle:
    print line

import number;
print number.fib()



