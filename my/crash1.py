
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
document = ["just", "a", "list", "of", "words"]
# different ways of counting, 1
word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0) # behave gracefully for missing keys
    word_counts[word] = previous_count + 1
# better solution with defaultdict
from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0
for word in document:
    word_counts[word] += 1
print word_counts

# Counter
from collections import Counter
c = Counter([0, 1, 2, 0]) # c is like a dictionary
word_counts = Counter(document)
# print the 10 most common words and their counts
for word, count in word_counts.most_common(10):
    print word, count

# Sets
s = set()
s.add(1) # s is now {1}
s.add(2) # s is now {1, 2}
s.add(2) # s is still {1, 2}
x = len(s) # equals 2
y = 2 in s # True
z = 3 in s # False
print x, y, z
# can use set to find distinct items in a list and for very fast search 'in' the set

# Control Flow
if 1 > 2:
    message = "if only oone were greater than two . . ."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
# ternary if-then-else
x=20
parity = "even" if x%2 == 0 else "odd"
# python while loop
x = 0
while x < 10:
    print x, " is less than 10"
    x += 1
# for + in
for x in range(10):
    if x == 3:
        continue # skip to next iteration
    if x == 5:
        break; # quit loop entirely
    print x

# Truthiness
one_is_less_than_two  = 1 < 2 # True
true_equals_false = True == False # False
print one_is_less_than_two, true_equals_false
# None is similar to null in other languages
x = None
print x == None # non-Pythonic way
print x is None # Pythonic way

# Falsy / Truthy
all([True, 1, { 3 }]) # True
all([True, 1, {}])    # False, {} is falsy
any([True, 1, {}])    # True, True is truthy
all([]) # True, no falsy elements in the list
any([]) # False, no truthy elements in the list

# Sorting
x = [4, 1, 2, 3]
y = sorted(x) # x unchanged
x.sort() # x changed
# sort the list by absolute value from largest to smallest
x = sorted([-4,1,-2,3], key = abs, reverse = True) # is [-4,3,-2,1]
# sort the word and counts from highest count to lowest
wc = sorted(word_counts.items(), key = lambda(word,count): count, reverse = True)

# List Comprehensions
even_numbers = [x for x in range(5) if x%2==0]
squares = [x*x for x in range(5)]
even_squares = [x*x for x in even_numbers]
print even_numbers, squares, even_squares
# similar for dictionaries or sets
square_dict = {x : x*x for x in range(5)}
square_set = {x*x for x in [1,-1]}
print square_dict, square_set
# user underscore as variable if the value from the list is not needed
zeroes = [0 for _ in even_numbers]
print zeroes
# multiple for loops
pairs = [(x,y)
         for x in range(10)
         for y in range(10)] # 100 pairs
print len(pairs), pairs
increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x+1, 10)] # later for can use  results of earlier one
print len(increasing_pairs), increasing_pairs



# Generators and Iterators
# use yield instead of range, in order to create elements as needed, without
# creating very long arrays
def lazy_range(n):
    """
    a lazy version of range
    :param n: number of elements to create range
    :return: a lazy iterator
    """
    i = 0
    while i < n:
        yield i
        i += 1
# consume yielded values one at a time until none are left
for i in lazy_range(10):
    print i
# xrange is a lazy version of range

# lazy generation using comprehensions wrapped in parantheses
lazy_events_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# in dict, user iteritems() instead of items() in order to get lazy yield of key-value pairs