### Some practice from video ###
my_range = range(5)
print(my_range)  # range(0, 5)
print(type(my_range))  # <class 'range'>
print(my_range[0])  # Accessing the first element: 0
print(my_range[-1])  # Accessing the last element: 4
print('----------')

# Iterating through the range and printing each value
for n in my_range:
    print(n, end=" ")  # Printing each value in the range on the same line
print()

# The result is the same if we define the range directly in the loop
for n in range(5):
    print(n, end=" ")
print()

# Using a range with a specific step
for n in range(12, 25, 5):  # start | stop | step
    print(n, end=" ")
print()

# Converting a range into other data structures
print(list(range(12, 25, 5)))  # Converts range to a list: [12, 17, 22]
print(tuple(range(12, 25, 5)))  # Converts range to a tuple: (12, 17, 22)
print(set(range(12, 25, 5)))  # Converts range to a set: {12, 17, 22}

# Attempting to convert a range to a dictionary will raise an error
# because a dictionary requires key-value pairs
# print(dict(range(12, 25, 5)))
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

# Working with range attributes
my_range_2 = range(5)
print(dir(my_range_2))  # Prints all available methods and attributes of the range object

print(my_range_2.start)  # Start value of the range
print(my_range_2.stop)  # End value of the range
print(my_range_2.step)  # Step value (default is 1)

# Creating a new range with a step
my_range_2 = range(10, 30, 3)
print(my_range_2.start)  # Start value: 10
print(my_range_2.stop)  # End value: 30
print(my_range_2.step)  # Step value: 3

# Finding the index of a specific value in the range
print(my_range_2.index(16))  # Returns the index of the value 16 (index is 2)

# Using the count method
# Since range contains only unique values, count will return either 0 or 1
print(my_range_2.count(10))  # Checks if 10 is in the range (returns 1 if found)

## Simple task
# Create a range and assign its values to a list
my_list = []  # Creating an empty list
for n in range(12, 98, 3):  # Iterating through the range
    my_list.append(n)  # Adding each value from the range to the list
print(my_list)  # Prints the final list

