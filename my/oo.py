
# create a Set class
# by convention we give PascalCase names
class Set:

    # member functions
    # every one takes a first parameter "self" (another convention)
    # that refers to the particular Set object (instance) being used

    def __init__(self, values = None):
        """
        This is the constructor.
        It gets called when you create a new set
        You would use it like
        s1 = Set() # empty set
        s2 = Set([1,2,2,3]) # initialize set with a list of values
        :return: Set
        """
        self.dict = {} # each instance of Set has its own dict property, which is what we'll use to track membership
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """
        This is the string representation of a Set object
        If you type it at the Python prompt or pass it to str().
        :return: a string
        """
        return "Set: " + str(self.dict.keys())

    # we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True

    # value is in the Set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

if __name__ == '__main__':
    s = Set([1,2,3])
    s.add(4)
    print s.contains(4) # True
    s.remove(3)
    print s.contains(3)
    print s