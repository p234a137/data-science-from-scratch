import random

# random.random() produces numbers uniformly between 0 and 1.
# It is one of the most used random functions.
four_uniform_randoms = [random.random() for _ in range(4)]

# pseudorandomness
random.seed(10)
print random.random() # 0.57140259469
print random.random()
random.seed(10)
print random.random() # 0.57140259469 again

# choose from an integer range
random.randrange(10) # choose from range(10)
random.randrange(3,6) # choose from range(3,6) = [3, 4, 5]

# randomly reorder elements of a list
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

# randomly pick element from a list
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print my_best_friend

# pick elements from a list without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers
# and with replacement
four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print four_with_replacement
