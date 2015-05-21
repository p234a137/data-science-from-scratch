
import random
documents = [random.randint(1,100) for _ in range(10)]

# not Pythonic
for i in range(len(documents)):
    document = documents[i]
    print i, document

# also not Pythonic
i = 0
for document in documents:
    print i, document
    i += 1

# Pythonic solution with enumerate
for i, document in enumerate(documents):
    print i, document

# if we just want the indices
for i in range(len(documents)): print i # not Pythonic
for i, _ in enumerate(documents): print i # Pythonic
