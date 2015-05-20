
# math
# integer division in python 2.X sucks
from __future__ import division
5/2

# the Zen of Python
import this

for i in [1, 2, 3, 4, 5]:
    print i
    for j in [10, 20, 30, 40, 50]:
        #print j
        print i + j
print "done looping"

# easy-to-read list declaration
list_of_lists = [ [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9] ]

# modules
# import a module
import re
my_regex = re.compile("[0-9]+, re.I")

#
import matplotlib.pyplot as plt
import numpy as np

#
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# functions
def double(x):
    """
    docstring, multiply input by 2 and return it
    """
    return x*2

def apply_to_one(f):
    """
    :param  function f
    :return: the function f with 1 as argument
    """
    return f(1)

# short anonymous functions using lambdas
y = apply_to_one(lambda x: x + 4)

# default values to functions
def my_print(message = "my default message"):
    print message

# names arguments
def subtract(a=0, b=0):
    return a - b

# strings
tab_string="\t"
len(tab_string) # is 1

# raw string, '\' and 't', not tab
not_tab_string = r"\t"
len(not_tab_string) # is 2

# Exceptions
try:
    print 0 / 0
except ZeroDivisionError:
    print "cannot divide by zero"


# Lists
integer_list = [1, 2, 3]
heterogenous_list = ["string", 0.1, True]
list_of_lists = [ integer_list, heterogenous_list, []]
list_length = len(integer_list)
list_sum = sum(integer_list)

x = range(10) # 0..9
zero = x[0]
one = x[1]
nine = x[-1] # 'Pythonic' for last element
eight = x[-2] # 'Pythonic' for next-to-last element
x[0] = -1 # set first element to -1
