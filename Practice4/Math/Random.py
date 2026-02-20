import random

print(random.random())
names = ["Ali", "John", "Sara"]
print(random.choice(names))
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)

print(cards)
