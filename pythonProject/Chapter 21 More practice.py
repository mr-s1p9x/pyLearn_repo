# Example 1: Immutable objects (e.g., strings and integers)
# If, for example, a string or an integer has the same value,
# they will refer to the same memory address in Python.
# This is due to Python's optimization for immutable objects.

from copy import deepcopy

number_1 = 10
number_2 = 10

print(id(number_1))  # e.g., 130876185638128
print(id(number_2))  # Same as above because integers are immutable

my_string_1 = 'Hello Python'
my_string_2 = 'Hello Python'

print(id(my_string_1))  # e.g., 127340959725680
print(id(my_string_2))  # Same as above because strings are immutable
# Immutable objects with the same value share the same memory address

print("========")

# Example 2: Mutable objects (e.g., lists)
# Mutable objects always have different memory addresses even if their values are the same
first_num = 1023
second_num = first_num

print(id(first_num))  # e.g., 129479243578000
print(id(second_num))  # Same as above because they reference the same integer

second_num += 5

print(id(first_num))  # Still the same as before
print(id(second_num))  # Different because a new integer was created for "second_num"

print("========")
print("Addresses of mutable objects")
my_list = [1, 2, 3]
print(id(my_list))  # Memory address of the first list

other_list = [1, 2, 3]
print(id(other_list))  # Different address because lists are mutable

print(id([1, 2, 3]))  # Another different address for a newly created list
# Lists are mutable, and every new list creation results in a unique memory address

print("========")
# Example 3: Working with dictionaries
info = {
    'name': 'Bogdan',
    'is_instructor': True
}

copy_info = info  # Shallow copy (direct reference)

print("Printing both dictionaries (one was copied from another)")
print(info)
print(copy_info)

# Adding a new key-value pair to "copy_info" affects both dictionaries
copy_info['rev_qty'] = 5

print("Printing both dictionaries after adding one pair into 'copy_info'")
print(info)
print(copy_info)

# Modifying a shared reference impacts both objects
info['rev_qty'] = 100
print(info)
print(copy_info)

# Are they equal in content?
print(info == copy_info)  # True
# Do they have the same memory address?
print(id(info) == id(copy_info))  # True

print("========")
# Creating independent dictionaries
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

# Both dictionaries have the same content but different memory addresses
print(id(info_1))  # One memory address
print(id(info_2))  # Different memory address
print(id(info_1) == id(info_2))  # False | Different objects

print("========")
# Example 4: Avoiding shared references
superhero = {
    'name': 'Peter',
    'superhero-name': 'Spider-Man',
    'place_to_live': 'New York'
}

# Shallow copy (direct reference to inner objects)
copy_superhero = superhero.copy()

# Adding a new key-value pair only affects "copy_superhero"
copy_superhero['suit'] = 'Spider-Man | 2077'

print(superhero)
print(copy_superhero)

# Different dictionary IDs
print(id(superhero))
print(id(copy_superhero))

print()
# Example 5: Shared references in nested structures
superhero_2 = {
    'name': 'Logan',
    'superhero-name': 'Wolverine',
    'place_to_live': 'Xavier University, Alberta, CA',
    'cite': []  # Nested mutable object
}

copy_superhero_2 = superhero_2.copy()
copy_superhero_2['cite'].append(
    "My whole life I felt like an animal. "
    "I ignored my instincts and I ignored what I really am."
)

# Both dictionaries share the same reference to the "cite" list
print(copy_superhero_2)
print(superhero_2)

# Different dictionary IDs but shared references for nested objects
print(id(copy_superhero_2))
print(id(superhero_2))

# Changing other keys won't affect the original
superhero_2['name'] = 'Spider'
print(copy_superhero_2)
print(superhero_2)

print()
# Example 6: Using deepcopy to avoid shared references
superhero_3 = {
    'name': 'Wade',
    'superhero-name': 'Deadpool',
    'city_to_live': 'New York',
    'cite': []
}

copy_superhero_3 = deepcopy(superhero_3)

# Different IDs = independent objects
print(id(copy_superhero_3))
print(id(superhero_3))

copy_superhero_3['cite'].append(
    "Life is an endless series of trainwrecks with only brief, "
    "commercial-like breaks of happiness"
)

# "cite" was added only to "copy_superhero_3"
print(copy_superhero_3)
print(superhero_3)  # Original remains unchanged
