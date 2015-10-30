#!/usr/bin/python
import math
print "My name is {0} and my age is {age}. I was born in {where}".format('viet',age=15, where='Tan Hoi')
print "The value of PI is approximately {}".format(math.pi)
print "The value of PI is approximate {!s}, or more precise: {!r}".format(math.pi, math.pi)
print "The value of PI is {0:.3f}".format(math.pi)
contact = {'viet':12345, 'huong':6886, 'hoang':2322, 'lam':23223}
for name, phone in contact.items():
	print "{0:10} ===> {1:10d}".format(name, phone)

print "format with a dictionary comes with 2 way"
print "{0[viet]:d}, {0[huong]:d}, {0[lam]:d}, {0[hoang]:d}".format(contact)
print "way 2, use dictionary as keyword arguments **"
print "viet: {viet:d}, huong: {huong:d}, hoang: {hoang:d}, lam: {lam:d}".format(**contact)

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
else:
	"Everything is fine"
	f.close()

class VietError(Exception):
	"""Here is docstring for class

		Attributes:
			value -- definition for class attribute is here
	"""

	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

try:
	raise VietError("hahahaha, just kidding error, for practising class")
except VietError as e:
	print "Error {0} occured: {1}".format(2,3)
	print "In fact, it is " + str(e)
else:
	print "No way for this line to come"
finally:
	print "Lol, finally is so weird"

print "what is called 'with open(fileName) as f' ? It's called predefined clean-up actions"
