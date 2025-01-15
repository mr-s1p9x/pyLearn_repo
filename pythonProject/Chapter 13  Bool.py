db_is_available = False

print((db_is_available))
print(type(db_is_available))     # <class 'bool>

db_is_available = True
print(db_is_available)

# Here is some boolean examples
print("=========")
print(bool(10))                  # True
print(bool('abc'))               # True
print(bool([]))                  # False
print(bool([1, 2]))              # True
print(bool(None))                # False

# Another boolean examples
print("=========")
print(100 > 10)                  # True
# Python compares symbolically
# by lexicographical order (like alphabet order)
# Python compares ASCII / Unicode value
# L has code 76, S has code 83
# So 76 not greater than 83, Python returns False
print("Long string" > "Short")   # False
print([] == [])                  # True
print([1, 2, 3] == [1, 2, 3])    # True
print({'a': 3} == {'a': 5})      # False