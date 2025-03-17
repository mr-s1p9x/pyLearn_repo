# 1. Handling ZeroDivisionError using try/except
# This example demonstrates how to catch an exception caused by division by zero.

try:
    print(10 / 0)  # Attempting to divide by zero, which will raise ZeroDivisionError
except ZeroDivisionError:
    print("Error - Division by zero")  # Handling the exception gracefully

print("Continue...")  # Ensuring the program continues executing after handling the error

print("\n===")

# 2. Assigning an exception to a variable
# This allows us to inspect the error object and retrieve additional information.

try:
    print(10 / 0)  # Attempting to divide by zero
except ZeroDivisionError as e:
    print(type(e))  # Outputs the error type: <class 'ZeroDivisionError'>
    print(dir(e))   # Lists available attributes and methods for the exception object
    print(e)        # Prints the default error message: 'division by zero'

print("Continue...")

print("\n===")

# 3. Handling multiple exception types
try:
    print('10' / 0)  # This will raise TypeError before reaching ZeroDivisionError
except ZeroDivisionError as e:
    print(e)  # Handles division by zero
except TypeError as e:
    print(type(e))  # Outputs: <class 'TypeError'>
    print(e)  # Prints the error message

print("Continue...")

print("\n===")

# 4. Using 'else' with try/except
try:
    print(10 / 5)  # Valid division, no error occurs
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("There was no error")  # This block runs if no exception occurs
finally:
    print("Continue...")  # 'finally' block always executes, regardless of errors

print("\n===")

# 5. Using a generic Exception handler
try:
    print(10 / 0)  # Attempting to divide by zero
except Exception as e:  # Catching any exception (not just ZeroDivisionError)
    print(e)  # Prints the error message

try:
    print(10 / 0)
except:
    print("Some error occurred")  # Catching any error without specifying type (not recommended)

print("\n===")

# 6. Using isinstance to check exception type
try:
    print(10 / 0)  # Attempting to divide by zero
except ZeroDivisionError as e:
    # Checking if 'e' is an instance of ZeroDivisionError class
    print(isinstance(e, ZeroDivisionError))  # True, if type was 'str' it would be False
    print(e)  # Prints the error message
except TypeError as e:
    print(e)  # Handles TypeError if it occurs

print("Continue...")
