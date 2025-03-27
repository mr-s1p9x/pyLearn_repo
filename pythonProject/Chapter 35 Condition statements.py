# IF statements
print("IF examples")

num_one = 10
num_two = 5

# Check if both numbers are positive integers
if (num_one > 0 and 
    num_two > 0 and 
    isinstance(num_one, int) and 
    isinstance(num_two, int)):
    print("Both numbers are ints and positive")

print()

# IF ELSE statements
print("IF ELSE examples")

my_phone = {
    'price': 200,
    'brand': 'HTC'
}

# Check if the phone has a brand
if my_phone.get('brand'):
    print("Phone's brand is", my_phone['brand'])
else:
    print("There is no phone brand")

print()

# IF ELIF statements
print("IF ELIF examples")

my_number = 10

# Check if the number is positive, negative, or zero
if my_number > 0:
    print("Digit is positive")
elif my_number < 0:
    print("Digit is negative")
else:
    print("Digit is 0")

print()

# Using IF in functions
print("Using IF in functions")

def nums_info(a, b):
    # Check if both arguments are integers
    if not isinstance(a, int) or not isinstance(b, int):
        return "One of the arguments is not INT"
    
    # Compare the numbers
    if a >= b:
        return f"{a} greater or equals {b}"
    
    return f"{a} less than {b}"

# IF ELIF ELSE example in a function
def nums_info_2(a, b):
    # Check if both arguments are integers
    if not isinstance(a, int) or not isinstance(b, int):
        info = "One of the arguments is not INT"
    elif a >= b:
        info = f"{a} greater or equals {b}"
    else:
        info = f"{a} less than {b}"
    
    return info

# Testing the functions
print(nums_info(True, 10))     # Invalid input
print(nums_info(10, 5))        # 10 >= 5
print(nums_info(3, 12))        # 3 < 12

print()

print(nums_info_2(False, 11))  # Invalid input
print(nums_info_2(101, 45))    # 101 >= 45
print(nums_info_2(5, 14))      # 5 < 14
