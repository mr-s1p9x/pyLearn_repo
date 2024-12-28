### Some practice after theory ###
# Sets don't have indexes.
my_set = {'apple', 'banana', 'lime'}
print(f'Default set: {my_set}')
# If we try to access an element by index, it will raise an error.
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

# Sets can contain different data types:
my_set_diff = {True, 'hello', 10, 10.345}
print(f'Set with different data types: {my_set_diff}')
print(f'Set type is: {type(my_set)}') # <class 'set'>

# If a set contains duplicate elements, only unique elements will be shown when printed.
my_num_set = {151, 152, 324, 151, 335, 152, 983, 213, 933, 983}
print(my_num_set) # Only unique numbers are shown
# An interesting fact: elements are not printed in the order they were added.
# Instead, their order depends on hash values.
# That's why sets are unordered collections in Python.

# Order doesn't matter in sets.
my_lib_1 = {'print', 'hello', 'Python'}
my_lib_2 = {'hello', 'Python', 'print'}
# These sets are considered equal, even though the elements are in a different order.
print(my_lib_1 == my_lib_2) # True
#