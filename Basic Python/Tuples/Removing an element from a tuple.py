# Removing an element from a tuple

x = (2, 5, 8, 2, 5, 8, 44, 0, 1, 3, 4, 44)
x = list(x)
x.remove(0)
x = tuple(x)
print(type(x))
