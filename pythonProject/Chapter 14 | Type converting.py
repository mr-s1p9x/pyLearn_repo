# "10" + 5
# 5 + "10"

float_num = 50.5
str_val = "abc"
# Magic methods
#print(float_num * str_val)

# calling that magic methods
print(float_num.__mul__(str_val)) # NotImplemented

# Multiplication method not implemented for string * float num
# so it will cause an error
# print(str_val.__rmul__(float_num))

# We can check documentation using __doc__ for classes
print(bool.__doc__)