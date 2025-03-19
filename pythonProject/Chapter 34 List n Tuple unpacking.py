# Unpacking a list into individual variables
my_list = [1, 2, 3]

first, second, third = my_list  # Each element is assigned to a separate variable
print(first)  # 1
print(second)  # 2
print(third)  # 3

# If the number of variables does not match the list length, a ValueError occurs
# Example: If we try to unpack into four variables, but the list has only three elements:
# ValueError: not enough values to unpack (expected 4, got 3)

print("\n")

# Unpacking also works with tuples using the same syntax
my_tuple = ('banana', 'orange', 'grape')
print(type(my_tuple))  # <class 'tuple'>

my_banana, my_orange, my_grape = my_tuple  # Assigning tuple values to individual variables
print(my_banana)  # banana
print(my_orange)  # orange
print(my_grape)  # grape

print("\n")

# Unpacking a dictionary into function arguments using **
user_profile = {
    'name': 'Artem',
    'comments_qty': 23
}

# Function with default argument handling
def user_info(name, comments_qty=0):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

# Using ** to unpack dictionary keys as function arguments
print(user_info(**user_profile))  # Output: Artem has 23 comments

print("\n")
# Unpacking a dictionary using *
user_data = ['Artem', 24]

def user_info_2(name, comments_qty): # in this case must to be exactly 2 elements 
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"

print(user_info_2(*user_data))
# we can also write as: ...(user_data[0], user_data[1])

# also we can write like this:
my_name, my_comments_qty = user_data
print(user_info_2(my_name, my_comments_qty))