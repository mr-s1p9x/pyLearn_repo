## if, for example, string or int has the same value
# they will refer to one, same address in memory
# this if for the Python optimization, because those objects immutable
# For example:
number_1 = 10
number_2 = 10

print(id(number_1)) # f.e. 130876185638128
print(id(number_2)) # the same as above

my_string_1 = 'Hello Python'
my_string_2 = 'Hello Python'

print(id(my_string_1)) # f.e. 127340959725680
print(id(my_string_2)) # the same as above
# those objects using one link to refer one address in memory
###############
print("========")

# more examples
first_num = 1023
second_num = first_num

print(id(first_num)) # f.e. 129479243578000
print(id(second_num)) # the same as above

second_num += 5

print(id(first_num)) # f.e. 129479243578000
print(id(second_num)) # different, f.e. 125358040064336

#### Addresses of mutable objects
print("========")
print("Addresses of mutable objects")
my_list = [1, 2, 3]
print(id(my_list)) # one id

other_list = [1, 2, 3]
print(id(other_list)) # different from above id

print(id([1, 2, 3])) # one more different id
# this happens because lists are mutable objects
# and every list creation will be assigned different address in memory
# even if objects in the lists are the same - Python will create
# new link (address in memory)

print("========")
# dictionary examples
info = {
    'name': 'Bogdan',
    'is_instructor': True
}

copy_info = info

print("Printing both dictionaries (one was copied from another")
print(info)
print(copy_info)

# Now add one pair into copy_info dict and print both
copy_info['rev_qty'] = 5

print("Printing both dictionaries after adding one pair into 'copy_info'")
print(info)
print(copy_info)
# and see that both dictionaries have 'rev_qty' string

print()
info['rev_qty'] = 100
# now both have 100
print(info)
print(copy_info)

# are they equal each other ?
print(info == copy_info) # True
# are they have the same id ?
print(id(info) == id(copy_info)) # True

print("========")
# But what if we need create different objects?
# we can just create separate objects with the same key-pairs
# but they will be different

info_1 = {
    'name': 'Stacy',
    'is_journalist': True,
    'city_to_live': 'New York'
}

info_2 = {
    'name': 'Stacy',
    'is_journalist': True,
    'city_to_live': 'New York'
}

# now lets see, if those objects are differ
print(id(info_1)) # One id
print(id(info_2)) # differ from above id

print(id(info_1) == id(info_2)) # False | different objects

