# Practice

input_str = input("Enter any number: ")
print(input_str)
print(type(input_str))       # <class 'str'>

input_int = int(input_str)   # Changing str to int
print(input_int)
print(type(input_int))        # <class 'int'>

# float numbers example
average_price = 17.25
print(average_price)          # 17.25
print(type(average_price))    # <class 'float'>

# Numbers conversion
# You can convert str, int, float
average_price = 28.75
price = int(average_price)
print(price)                  # 28
print(type(price))            # <class 'int'>

str_temperature = "14.5"
temperature = float(str_temperature)
print(temperature)            # 14.5
print(type(temperature))      # <class 'float'>

# Rounding numbers
# Rounding to the nearest integer
average_price = 17.25
print(round(average_price))   # 17

rate = 0.78
print(round(rate))             # 1
print(type(round(rate)))       # <class 'int'>

# Complex numbers
complex_a = 10 + 7j
complex_b = 3 + 3j
print(complex_a + complex_b)

