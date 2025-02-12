my_list = [1, 2]
other_list = ['a', 'b']

# We get values from the first list because both lists are non-empty (truthy).
# The OR operator returns the first truthy value and skips the rest.
print(my_list or other_list)

# Another way to write it:
# Returns the first truthy value
print(len(my_list) > 0 or other_list)

# Let's check this:
print(len(my_list) < 0 or other_list)  # Returns ['a', 'b']

#####

my_dict = {}

# Returns an empty dictionary because an empty dict is considered False.
print(my_list and my_dict)

# We can convert it to a boolean and check:
print(bool(my_list and my_dict))  # False

# Another example:
my_list_2 = [1, 2, 3]

# The AND operator executes the second operand if the first one is truthy.
# So, "List is not empty" will be printed.
my_list_2 and print("List is not empty")

# Task for practice:
# Create two dictionaries with the same keys.
# Using the 'and' operator, print "Dictionaries are equal" if the first dictionary is equal to the second one.

car_specs_1 = {
    'brand': 'Toyota',
    'color': 'White',
    'price': 15000,
}

car_specs_2 = {
    'brand': 'Toyota',
    'price': 15000,
    'color': 'White'
}

# The condition checks if both dictionaries are equal.
# If they are, "Dictionaries are equal" will be printed.
car_specs_1 == car_specs_2 and print("Dictionaries are equal")
