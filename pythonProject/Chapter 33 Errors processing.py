# 1. Handling ZeroDivisionError using try/except
# This example demonstrates how to catch an exception caused by division by zero.

try:
    print(10 / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error - Division by zero")  # Handling the exception gracefully

print("Continue...")  # Ensuring the program continues executing after handling the error


# 2. Assigning an exception to a variable
# This allows us to inspect the error object and retrieve additional information.

try:
    print(10 / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(type(e))  # Outputs the error type: <class 'ZeroDivisionError'>
    print(dir(e))   # Lists available attributes and methods for the exception object
    print(e)        # Prints the default error message: 'division by zero'

print("Continue...")  # The program continues execution after handling the error
