
# apply or curry functions to create new functions
def exp(base, power):
    return base**power

#def two_to_the(power):
#    return exp(2, power)

# using functools
from functools import partial
two_to_the = partial(exp, 2) # is now a function of one variable
print two_to_the(3)


# map, reduce, and filter provide functional alternatives to list comprehensions
def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2,4,6,8]
twice_xs2 = map(double, xs) # same as above list comprehension
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs3 = list_doubler(xs) # same as above
print twice_xs, twice_xs2, twice_xs3

# multiple-argument functions
def multiply(x, y): return x*y
products = map(multiply, [1,2], [4,5]) # [1*4, 2*5] = [4,10]
print products

# filter
def is_even(x):
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens2 = filter(is_even, xs) # same, using filter
list_evener = partial(filter, is_even) # function that filters a list
x_evens3 = list_evener(xs)    # same as above
print x_evens, x_evens2, x_evens3

# reduce combines the first two elements of a list, then that result with the third,
# that result with the fourth, and so on, producing a single result.
x_product = reduce(multiply, xs) # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list through multiplication
x_product2 = list_product(xs)    # again 24
print x_product, x_product2
