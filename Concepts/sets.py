# Sets and Methods
# Set is a da1ta1 type in python used to store several items in a single varia1ble.
# It is a collection that is written with curly brackets and is both
# un indexed and unordered. Does not allow duplicate value

a1 = {3, 5, 23, 34, 5, 5, 5}
a2 = {3, 5, 7, 8, 9}
print(a1.pop())
a1.add(9)
print(a1)
print(a1.union(a2))
print(a1.intersection(a2))

# empty set -> set() and empty dict -> {}