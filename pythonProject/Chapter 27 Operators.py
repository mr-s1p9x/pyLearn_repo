a = [1, 2]
b = [1, 2]
print(a == b) # True
print(a.__eq__(b)) # True | magic method

# if we print __eq__ w/o compare - it will show object address in memory
print(a.__eq__) # <method-wrapper '__eq__' of list object at 0x000001F54B156040>

print(id(a) == id(b)) # False | different id's
print(f'id a: {id(a)}')
print(f'id b: {id(b)}')

# also different addresses in memory
print(f'hex a: {hex(id(a))}')
print(f'hex b: {hex(id(b))}')

# examples with unary operators

my_num = 10
print(+my_num) # clearly converts into int 

my_bool = True
print(+my_bool) # clearly converts into int

# if 'not' = False, for example
my_num_2 = 10 # Obviously True
print(not my_num_2) # if not then False

my_num_2 = 0 # Obviously False
print(not my_num_2) # if not False then - True

print()
# Example of in, not in operators
my_car = {
    'brand': 'Toyota',
    'price': 10000
}
# checking the existence  of an object in dict
print('brand' in my_car) # True
print('year' in my_car) # False
print('year' not in my_car) # True