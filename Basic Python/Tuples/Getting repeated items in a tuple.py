# Getting repeated items in a tuple

x = (2, 5, 8, 2, 5, 8, 44, 0, 1, 3, 4, 44)
x = list(x)
dups = []
for i in range(len(x)):
    if x.count(x[i]) > 1:
        dups.append(x[i])

print(set(dups))
