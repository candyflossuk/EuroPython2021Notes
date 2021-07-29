"""
Notes from the pydonts talk from EuroPython 2021
"""

# Naming
"""
Naming can be what the object does or some major property from the object.
"""

# Enumeration

# One example
my_list = []
for elem in my_list:
    print(elem)

# Traverse list with indices
for idx in range(len(my_list)):
    elem = my_list[idx]
    print(idx, elem)

# Instead of using this you can use
for idx, elem in enumerate(my_list):
    print(idx, elem)

# You can also use zip for for loops



