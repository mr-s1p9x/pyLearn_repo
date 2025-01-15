### Practice from video ###

# Creating lists of fruits and their corresponding quantities
fruits = ['apple', 'banana', 'lime']
quantities = [100, 70, 50]

# Now let's combine these two lists using the zip function
# The zip function creates pairs of elements as tuples by default
fruits_qtys_zip = zip(fruits, quantities)

# If we print the zip object directly, we get its memory address
print(fruits_qtys_zip)  # <zip object at 0x7.......>
# Printing the type of the zip object
print(type(fruits_qtys_zip))  # <class 'zip'>

# To see the actual combined elements, we need to convert the zip object to a list (or another iterable)
fruits_qtys_list = list(fruits_qtys_zip)
print(fruits_qtys_list)  # [('apple', 100), ('banana', 70), ('lime', 50)]

# Another zip example with more data
my_fruits = ['orange', 'grape', 'banana', 'lime', 'mango']
my_qtys = [100, 500, 70, 30, 50]
my_bool = [True, False, False, True, True]

# Zipping three lists together: fruits, quantities, and boolean values
my_mix_zip = zip(my_fruits, my_qtys, my_bool)
print(my_mix_zip)  # <zip object at 0x7......>

# Converting the zip object to a list to see the combined elements
my_mix_list = list(my_mix_zip)
print(my_mix_list)
# Output: [('orange', 100, True), ('grape', 500, False), ('banana', 70, False), ('lime', 30, True), ('mango', 50, True)]

print("==========================")

# Zip also works with mixed data structures, like lists, tuples, and sets
hardware = ['computer', 'laptop', 'notebook']  # List of hardware items
h_qtys = {100, 50, 130}  # Set of quantities (unordered)
h_availability = (True, False, True)  # Tuple of availability (ordered)

# Combining the above data structures into a zip object
h_zip = zip(hardware, h_qtys, h_availability)
h_list = list(h_zip)  # Converting the zip object to a list

# Printing each combined element with a position number
count = 1
print("Hardware available: ")
for n in range(len(h_list)):
    print(f'Position {count}# : {h_list[n]}')  # Example output: Position 1#: ('computer', 100, True)
    count += 1

# One more example: converting a zip object into a dictionary
list_1 = ['banana', 'apple', 'grape']  # List of items
qtys_1 = [100, 60, 70]  # List of quantities

# Zipping the two lists together and converting them into a dictionary
zip_list = zip(list_1, qtys_1)
dict_list = dict(zip_list)  # The keys will be items from list_1, and the values will be from qtys_1
print(dict_list)
# Output: {'banana': 100, 'apple': 60, 'grape': 70}
