#!/usr/bin/python
a = [66.25, 333, 333,  1, 1234.5]
print a.count(333), a.count(1234.5), a.count('x')
a.insert(2, -1)
a.append(333)
print a
a.extend([-1])
print a
a.pop()
print a
a.pop(2)
print a
a.reverse()
print a
a.sort() #asc
print a
a.remove(333) #remove first 2 in the list
print a
del a[:2]
print a

print "Using list as a stack with append and pop"
print "Using list as a queue is not appropiated since append and pop from beginning of the list is slow"
from collections import deque
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue.popleft()
queue.popleft()
print queue

print "Playing with filter, map and reduce"
def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, range(0,20))

print "Compute some cubes with map:"
def g(x): return x * x * x
print map(g, range(5))

print ("my beautiful example with map:")
def h(x, y, z): return x + " " + y + " " + z
print map(h, ["Viet", "Hoang", "Lam"], ["loves", "hates", "teases"], ["TH", "OL", "TE"])

print "I don't like reduce function"
print "Use sum instead"
def add(x, y): return x + y
print reduce(add, range(1,10))

print "List comprehension is so interesting"
print "You can beautiful establish a list like this"
squares1 = [x ** 2 for x in range(10)]
squares2 = map(lambda x: x ** 3, range(10))
print squares1
print squares2

print "Build list of tuples like this"
relatives = [(x,y) for x in range(1,20) for y in range(1,20) if x % y == 0]
print relatives

print  "Zip matrix like that"
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
zipped_matrix = [[row[i] for row in matrix] for i in range(4)]
print zipped_matrix


print "Tuple is a special data of python, it's immutable, sequence of value separated by comma"
my_full_name = 'nguyen', 'hoang', 'viet'
print my_full_name
print "Tuple with one element"
birthday = 12,
print birthday
last, middle, first = my_full_name
print "My first name is", first

print "A set is an unordered collection with no duplicate elements"
set1 = set('asdfsjfrisfa')
set2 = set("slfjiowflalskfasdf")
print set1
print set2 
print "set1 - set2", set1 - set2
print "set 1 | set 2", set1 | set2
print "set1 ^ set2", set1 ^ set2
print "set1 & set2", set1 & set2
set3 = {1,12,3,42,12,1,2,1,41,42}
print set3
print "Set comprehension"
set4 = {x for x in "sljfasljfhsohfjjfwjw"}
print set4

print "Dictionary = hash in perl"
me = {'age':24, 'name':"viet", 'sex':'male'}
print me
quan = dict(age=24, name='quan', sex='male');
print quan

print "Dictionary comprehension example is so ugly"
ehem = {x:y for x in range(4) for y in range(100) if x ** 2 == y}
print ehem

print "Looping technique: enumeric, zip and reversed example"
for i, v in enumerate(sorted(reversed(range(10)))):
	print i, 'is', v

print "Looping two sequences at the same time"
questions = 'name', 'age', 'sex'
answers = 'huong', 26, 'male'

for q, a in zip(questions, answers):
	print 'What is your {0} ? It is {1}'.format(q,a)


print "Loop for dictionay:"
for k, v in me.iteritems():
	print k, v

print "Change a sequence you're iterating over inside the loop, you slice notation instead of normal way!!!"
print "Because slice notation will create a copy of sequence, we infact iterates over this copy"
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
    	words.insert(0, w)

print words