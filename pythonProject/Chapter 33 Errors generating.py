
def divide_nums(a, b):
    # Check if the second argument (b) is zero
    if b == 0:
        # If b is zero, raise a TypeError with a custom message
        raise TypeError("Second argument can't be 0")
    
    # Perform the division if no error occurs
    return a / b

# Handling possible exceptions
try:
    divide_nums(10, 0)  # Attempt to divide 10 by 0, which triggers an exception
except ZeroDivisionError as e:
    # This block catches ZeroDivisionError, but it won't be triggered
    print(e)
except TypeError as e:
    # This block catches TypeError, which is raised when b == 0
    print(e)  # Output: "Second argument can't be 0"

# This statement executes regardless of whether an exception occurred or not
print("Continue...")  # Output: "Continue"

# Example 2: With ValueError
def divide_nums(a, b):
    # Check if the second argument (b) is zero
    if b == 0:
        # If b is zero, raise a ValueError with a custom message
        raise ValueError("Second argument can't be 0")
    
    # Perform the division if no error occurs
    return a / b

# Handling possible exceptions
try:
    divide_nums(10, 0)  # Attempt to divide 10 by 0, which triggers an exception
except ZeroDivisionError as e:
    # This block catches ZeroDivisionError, but it won't be triggered
    print(e)
except ValueError as e:
    # This block catches ValueError, which is raised when b == 0
    print(e)  # Output: "Second argument can't be 0"

# This statement executes regardless of whether an exception occurred or not
print("Continue...")  # Output: "Continue"
