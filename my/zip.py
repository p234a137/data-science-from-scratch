# zip and Argument unpacking

# zip two or more lists together into a single list of tuples of corresponding elements
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print zip(list1, list2) # [('a', 1), ('b', 2), ('c' 3)]

# unzip using a strange trick
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs) # * does argument unpacking
print letters, numbers

# re-use the * trick
def add(a, b): return a + b
print add(1,2) # 3
#print add([1,2]) # type error
print add(*[1,2]) # 3

