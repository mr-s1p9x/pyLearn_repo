my_list = [1, 2]

# We must use del separatly from 'print' or 'return' 
# or we can get 'invalid syntax' error
del my_list[0]

# also we can delete like this, using magic method
my_list.__delitem__(0)

print(my_list)
