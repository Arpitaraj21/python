# List and Methods
# list ->  A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements
# can have multiple data types

l1 = [5, 1, 234, 234, 234]
print(type(l1))
print(l1)

# O/P > <class 'list'>
# [3, 5, 234, 234, 234]

# NOTE -> String is immutable isliye har baar methods use karne se pycharm
# ek new string banata hai but that is not the case with list agar koi chiz
# change hota hai toh vo directly uss list me change hota hai

# methods
# l1.remove(234)
# print(l1)


print(l1.count(234))

l1.sort()
print(l1)

l1.pop()
print(l1)

l1.append(78) # adds value at end
print(l1)

l1.extend([67,34,76,89])
print(l1)

print(l1.index(89))

print(l1[0:3])