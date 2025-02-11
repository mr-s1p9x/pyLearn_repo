# Using docstring
def print_number_info(num):
    """
    Prints num information      

    Args:   
        num (int): Integer number 

    Returns:
        int: Same number
    """
    if (num % 2) == 0:
        print("Num is even")
    else:
        print("Num is odd")

    return num

print_number_info(2)


# more practice
c = 5

def my_fn(a, b):
    d = 10
    print(c)
    print(a, b)
    print(dir())

my_fn(3, 5)

