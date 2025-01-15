# creating empy dictionary
my_disk = {}

print(id(my_disk)) # printing id | address in memory
print(type(my_disk)) # printing type of that dictionary | <class 'dict'>

# adding some keys to our dictionary
my_disk['brand'] = 'Samsung'
my_disk['price'] = 80

print(my_disk) # printing it
print(id(my_disk)) # id remain the same, caz we're modifying an existing object

# methods for dictionaries
print(my_disk.items()) # dict_items([('brand', 'Samsung'), ('price', 80)])
print(my_disk.keys()) # dict_keys(['brand', 'price'])

# popitem removes last added key
# you don't know which element was added last
# so this method is not recommended
print(my_disk.popitem()) # this method removed one element from dict, it shows which removed
print(my_disk)

print(my_disk.get('type')) # None if non-existing key

# Practice, copying dictionary
# it's usefull when you want to work with a dictionary
# but doesn't want to change original object
new_disk = my_disk.copy()
# creating new key for a dictionary copy
new_disk['type'] = 'ssd'

# printing both
# and see that disks has a different id's
print(f'my_disk: {my_disk}, id: {id(my_disk)}')
print(f'new_disk: {new_disk}, id: {id(new_disk)}')

print(len(new_disk))

#####################################################
my_list2 = [['first', 10], ['gold', True]]

# that thing will also work
# my_list2 = [('first', 10), ('gold', True)]

# dict() function can create dictionaries from a list of lists
# (or other iterable structure), if each nested element is a (key, value) pair
# But if the list contains single elements, dict() will print an error, because
# it cannot recognize them as pairs
my_dict = dict(my_list2)

# We also cannot create dictionary from string
# that won't work
# my_str = 'abcd'
# my_dict = dict(my_str)

print(my_dict)


