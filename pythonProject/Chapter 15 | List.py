my_fruits = ['apple', 'orange', 'banana']
posts_ids = [151, 234, 321, 532]

# Calculating length of each list
print(len(my_fruits))
print(len(posts_ids))

# printing value of list by id
print(my_fruits[1])
print(posts_ids[3])
# printing last value from list
print(my_fruits[-1])
print(posts_ids[-1])

# order in list is valuable thing
list_1 = ['apple', 'banana', 'grape']
list_2 = ['apple', 'grape', 'banana']
# the same values, but different order

# try to compare them
print(list_1 == list_2) # False
# We're getting False, because order play important role

# but if we compare those lists - we'll get True
list_3 = ['apple', 'banana', 'grape']
print(list_1 == list_3) # True

# We can change values in list
print("=== Changing ===")
list_3[2] = 'kiwi'
print(list_3)

# We can also delete values in list
print("=== Deleting ===")
print(my_fruits)
del my_fruits[1]
print(my_fruits)

print()
# lists of dictionaries
# pairs with key:value
users = [
    {
        'user_id': 134,
        'user_name': 'John'
    },
    {
        'user_id': 135,
        'user_name': 'Will'
    }
]

print(users)
print(len(users)) # 2 Users
# Partial print
print(users[0]['user_name']) # John
print(users[1]['user_id'])   # 135

# PRACTICE =============================

my_nums = [10, 50, 0, 5, 5, 100]
print(type(my_nums)) # <class 'list'>

# to check all avalable attributes for my_nums we can use 'dir'
print(dir(my_nums))

# we can count the same numbers
res = my_nums.count(5)
print(res) # 2

# adding some numbers to the list
my_nums.append(25)
print(my_nums)

# insert object before index
my_nums.insert(2, -5) # index/value
print(my_nums)

# we can clear whole list using .clear method
# my_nums.clear()
# print(my_nums) # []

# we can extend list by appending elements from the iterable
# elements from other sequences
my_nums.extend('abc')
print(my_nums) # [..., 'a', 'b', 'c']

# using copy method to create new object id
other_nums = my_nums.copy()

print(id(my_nums))
print(id(other_nums))

my_nums.append(3)
other_nums.clear()

print("=====")
# we can also use slice for copy lists
other_nums = my_nums[:] # or use method list to create new object list(my_nums)
print(id(my_nums))
print(id(other_nums))

my_nums.append(3)
other_nums.clear()

print(my_nums, other_nums)
