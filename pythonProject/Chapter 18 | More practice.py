my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

# Finding common elements from both set's
print(my_set.intersection(other_set)) # {'f', 'd'}
print(other_set.intersection(my_set)) # same result as above

# We can also provide with an argument as string
print(my_set.intersection('abcd')) # {'d'}

# And we can also provide with a list as argument
print(my_set.intersection(['a', 'b', 'c', 'd'])) # {'d'}
# And tuple
print(my_set.intersection(('a', 'b', 'c', 'd'))) # {'d'}

# Adding sets
print(my_set.union(other_set)) # {'f', 'a', 'd', 'y', 'abc'}

# checking if other_set containing all the same elements as my_set
# other_set is not a subset of my_set
print(other_set.issubset(my_set)) # False

# We can remove 'a' element and get True, because my_set doesn't contain 'a'
# using .remove, we need exact element, but we don't know order of it
other_set.remove('a') # pop could be useful if order of deletion is not important
print(other_set)
# checking again
print(other_set.issubset(my_set)) # True

# using in other sequence | is my_set is superset for other_set ?
print(my_set.issuperset(other_set)) # True

# Both methods .issuperset and .issubset will work for True of sets are the same:
my_set = {'d', 'f'}
other_set = {'d', 'f'}
print(other_set.issubset(my_set)) # True
print(my_set.issuperset(other_set)) # True

# difference method will show the difference between two set
my_set = {'abc', 'd', 'f', 'y'}
other_set = {'a', 'f', 'd'}

# shows the difference, which exists in 1st list, and upset in second
print(my_set.difference(other_set)) # {'y', 'abc'}

# allow to remove objects from set
print(my_set.discard('d'))
print(my_set) # {'y', 'abc', 'f'}

# if we try to remove non-existing object - we will get an error
#my_set.remove('def') # KeyError: 'def'
# but if object exist - it will remove it
my_set.remove('abc')
print(my_set) # {'f', 'y'}

# we can copy sets
copied_set = my_set.copy()

# adding some elements into both
my_set.add('t')
copied_set.add('l')
# and print them
print(my_set) # {'y', 'f', 't'}
print(copied_set) # {'y', 'f', 'l'}

# These are the elements that are not shared between the two sets
print(my_set.symmetric_difference(copied_set)) # {'t', 'l'}

##########################################################

a = {'abc', 'd', 'f', 'y'}
b = {'abc', 'd', 'f', 'l'}

print(a.union(b)) # Combines all unique elements from both sets
print(a.intersection(b)) # Finds common elements between the two sets

# {'abc', 'd', 'f', 'l', 'y'} - {'abc', 'd', 'f'} = {'l', 'y'}
print((a | b) - (a & b)) # {'l', 'y'}
# The above operation is equivalent to a.symmetric_difference(b)
