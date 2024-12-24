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

# we can check all available attributes for our object
# but it won't show price, brand etc - it's important
print(dir(my_motorbike))

# adding new keys to the dictionary
my_motorbike['color'] = 'green' # adding color
my_motorbike['is_new'] = True # adding wear parameter
print(my_motorbike)

# deleting elements
del my_motorbike['color']
print(my_motorbike)

# Access to value using variable
# we can create a variable and assign it our key-value
key_brand = 'brand'
key_color = 'color'
key_price = 'price'

my_motorbike[key_brand] = 'Honda' # changing brand name
my_motorbike[key_color] = 'blue' # if there is no key - it will create new
my_motorbike[key_price] = 7000 # changing price
print(my_motorbike)
# {'brand': 'Honda', 'price': 7000, 'engine_vol': 1.2, 'is_new': True, 'color': 'blue'}

# Nested dictionaries
# Value in dictionary can be also a dictionary:
del my_motorbike['price'] # first of all delete price, we will create the new one
my_motorbike['price_info'] = {'price': 25000, 'is_available': True} # adding new values
print(my_motorbike) # {...'color': 'blue', 'price_info': {'price': 25000, 'is_available': True}}

# and we can also get info and change those values
# print (get) some info
print(my_motorbike['price_info']['price']) # 25k
print(my_motorbike['price_info']['is_available']) # True

# and change those values
my_motorbike['price_info']['price'] = 20000
my_motorbike['price_info']['is_available'] = False
print(my_motorbike['price_info']['price']) # 20k
print(my_motorbike['price_info']['is_available']) # False

# we can also create dictionary using variables, for example
# variables
car_brand = 'Honda'
car_model = 'S2000'
engine_vol = 2.0
car_color = 'white'
car_price = 10000

# dictionary creation
my_car = {
    'brand': car_brand,
    'model': car_model,
    'engine_vol': engine_vol,
    'color': car_color,
    'price': car_price
}
print(my_car)

# dictionary length
# len() is also working for the dictionaries
print(len(my_car)) # 5
del my_car['color']
print(len(my_car)) # 4

# no existing key
# if we refer to a non-existent key - we'll get an error
# print(my_car['tires']) # KeyError: 'tires'

# more secure method get
# we can use get method for displaying the key, and if the key doesn't exist
# we won't get an error
print(my_motorbike.get('model')) # None

# and we can also change default get output by writing the second parameter
print(my_motorbike.get('model', 0)) # 0
print(my_motorbike.get('model', 'this key doesn\'t exist')) # string message