# Write a Python program to import built-in python module and display the namespace of the said module
# In this case I've used the time module


import time as m

for name in m.__dict__:
    print(name)
