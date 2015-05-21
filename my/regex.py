import re

print all([
    not re.match("a", "cat"), # 'cat' does not start with an 'a'
    re.search("a", "cat"),    # 'cat' has an 'a' in it
    not re.search("c", "dog"), # 'dog' does not have a 'c' in it
    3 == len(re.split("[ab]", "carbs")), # split on 'a' or 'b' to ['c', 'r', 's']
    "R-D-" == re.sub("[0-9]", "-", "R2D2") # replace digits with dashes

])
