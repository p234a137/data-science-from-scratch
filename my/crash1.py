
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
# slicing
first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]
# operator to check list membership
1 in [1, 2, 3] # True
0 in [1, 2, 3] # False
# concatenate
x = [1, 2, 3]
x.extend([4, 5, 6])
x = [1, 2, 3]
y = x + [4, 5, 6]
x = [1, 2, 3]
x.append(0)
y = x[-1] # 0
z = len(x)
# list unpacking
x, y = [1, 2]
print x, y
_, y = 1, 2 # _ is a value we throw away

# tuples
my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3,4
try:
    my_tuple[1] = 3
except TypeError:
    print "Cannot modify a tuple"
# return multiple value from functions using tuples
def sum_and_product(x, y):
    return (x+y), (x*y)
sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)
x, y = 1, 2 # x=1, y=2
x, y = y, x # x=2, y=1

# dictionaries
empty_dict = {} # 'Pythonic' way of initialization
empty_dict2 = dict() # less Pythonic
grades = {"Joel" : 80, "Tim" : 95}
print grades
#
joels_grade = grades["Joel"]
try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"
# check existence of a key
joel_has_grade = "Joel" in grades # True
kate_has_grade = "Kate" in grades # False
# get method with default return value
joels_grade = grades.get("Joel", 0) # 80
kates_grade = grades.get("Kate", 0) # 0
no_ones_grade = grades.get("No One") # default default is None
print joels_grade, kates_grade, no_ones_grade
#
grades["Tim"] = 99 # replaces old values
grades["Kate"] = 100 # adds a third entry
num_students = len(grades)
print grades
# dictionaries as simple ways to represent structured data
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#datascience", "#science", "awesome", "#yolo"]
}
tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items() # list of (key, value) tuples

# defaultdict