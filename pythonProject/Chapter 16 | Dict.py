# Dictionaries

# the order is not important in dictionaries in Python
# for example, let's create 2 objects and their params will be in different order
my_motorbike = {
    'brand': 'Ducati',
    'price': 25000,
    'engine_vol': 1.2
}

other_motorbike = {
    'price': 25000,
    'engine_vol': 1.2,
    'brand': 'Ducati'
}

# now let's answer for some questions
# are these objects are the same (parameters) ?
print(my_motorbike == other_motorbike) # True, the same | order doesn't matter
# are these objects are different objects (id's)
print(id(my_motorbike) == id(other_motorbike)) # False | different object id's

# We can get some values from the dictionary
print(my_motorbike['price']) # It's important to write a string in params
# because if we remove the quotes, python will understand that as variable
# but we don't have a variable, it's just a key
print(my_motorbike['brand'])
print(other_motorbike['engine_vol'])

# for chaning values using the same pair [ ] and ' '
my_motorbike['price'] = 20000
my_motorbike['brand'] = 'Ducati Sport'
print(my_motorbike['price'])
print(my_motorbike['brand'])
