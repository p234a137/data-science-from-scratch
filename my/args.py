
# create a higher-order function that takes as input some function f and returns a new
# function that for any input returns twice the value of f

def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)
print g(3)
print g(-1)

# the above schema breaks down for function f of more than one variable
# use argument unpacking and a bit of magic
def magic(*args, **kwargs):
    print "unnamed args: ", args  # tuple of unnames arguments
    print "keyword args:", kwargs # dict of names arguments

magic(1, 2, key="word", key2="word2")

# this works the other way round too
def other_way_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z" : 3}
print other_way_magic(*x_y_list, **z_dict)

# use the trick just for defining higher-order functions that can accept arbitrary arguments
def doubler_correct(f):
    """
    works no matter what kind of input f expects

    :param f: function
    :return:double the value of f
    """
    def g(*args, **kwargs):
        """ whatever argument g is supplied, pass them to f """
        return 2 * f(*args, **kwargs)
    return g

def f2(x, y): return x+y

g = doubler_correct(f2)
print g(1, 2) # 6