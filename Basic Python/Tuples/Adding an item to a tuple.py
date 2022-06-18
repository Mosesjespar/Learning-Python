# Adding an item to a tuple

x = ('hey', 3, 4.66, True)
x = list(x)
x.append('mj')
x = tuple(x)
print(x)

# OR 
# x = x + ('mj', )