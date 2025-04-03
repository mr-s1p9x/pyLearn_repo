for el in [1, 'abc', True]:
    print(type(el))
    print(el)

# if we print 'el' here, it creates with the last parameter
print(el) # True

# and if we print dir() - we'll see 'el' here
# so it says that 'el' was created globally
print(dir())

# so better do not use the same name for the cycle variable 'el' 
# if variable with the same name was created somewhere earlier (before that cycle)


# dictionary example
my_dict = {
    'id': 324,
    'title': 'art'
}

for key in my_dict:
    print(type(key))
    print(key, my_dict[key])