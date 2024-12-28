my_nums = (10, 5, 100, 0, 5, 5)

print(type(my_nums)) # <class 'tuple'>
# we cannot change objects in tuple
# my_nums[1] = 7 # TypeError: 'tuple' object does not support item assignment

# also we cannot delete objects
# del my_nums[2] # TypeError: 'tuple' object doesn't support item deletion

post_ids = (10, 5, 20, 313, 4, 90)
index_to_chk = 2

if index_to_chk < len(post_ids) - 1:
    print('Index exists')
else:
    print('No such index')

### More practice ###
print(my_nums.count(5)) # 3
print(my_nums.index(5)) # index [1]
# what if we need to get index of 2nd and 3rd '5' ?
# because default .index shows only 1st index
# we can create a variable and assign our 1st index to id
first_entry = my_nums.index(5) # created
# then we do another move and can provide the 2nd argument, 'start' argument
# that will allow us skip this and start from that index and search another
# we need 'first_entry + 1' to skip this and go ahead
# otherwise we get the same index as before
second_enry = my_nums.index(5, first_entry + 1)
print(second_enry) # 4

# using converting into list and back we can add or delete some elements
my_nums = list(my_nums)
my_nums.append(103)
my_nums.append(987)
# printing to doublecheck
print(my_nums)
# and converting back
my_nums = tuple(my_nums)
print(my_nums)

# creating tuple example, we can provide with any sequences in it
my_tuple = tuple('abcdef#J/?2!')
print(my_tuple) # ('a', 'b', 'c', 'd', 'e', 'f', '#', 'J', '/', '?', '2', '!')

# we can also provide with a dictionary
my_tuple_2 = tuple({'first': 'Hello', 'second': 10})
print(my_tuple_2) # ('first', 'second')

# create tuple with different types
# then create one more tuple
# and adding them up using + operator
tuple_1 = (10, True, 'Sun', 10.234, 'Welcome, python!')
tuple_2 = (False, 'Weather', 1023.19290, 101, 'code!')
print(tuple_1)
print(tuple_2)
main_tuple = tuple_1 + tuple_2
print(main_tuple)