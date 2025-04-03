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

print()
# using .items() example
for item in my_dict.items():
    key, value = item
    print(key, value)

print()
# we can also use this method: [tuple unpacking]
for key, value in my_dict.items():
    print(key, value)

print()
# FOR IN for SET
video_ids =  {1435, 4317, 2739, 5403}

for id in video_ids:
    print(id)


# Some practice
for num in range(1, 31):
    print(num, end=' ')

print()

for step in range(1, 100, 5):
    print(step, end=' ')