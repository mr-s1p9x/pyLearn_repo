grey_button = {
    'width': 200,
    'text': 'Buy',
    'color': 'Grey'
}

# Creating a new dictionary based on grey_button and modifying the color
red_button = {
    **grey_button,  # Unpacking all key-value pairs from grey_button
    'color': 'Red'  # Overwriting the 'color' key
}

# {'width': 200, 'text': 'Buy', 'color': 'Red'}
print(red_button)

# The original dictionary remains unchanged
# {'width': 200, 'text': 'Buy', 'color': 'Grey'}
print(grey_button)

##### Another example #####

style_button = {
    'width': 200,
    'height': 300,
    'color': 'green'
}

info_button = {
    'action': 'Buy',
}

# Merging two dictionaries using the | (union) operator
final_button = style_button | info_button
print(final_button)

## Practice task
# Create 3 dictionaries and merge them using |

name_button = {
    'name': 'Buy button'
}

style_of_button = {
    'width': 400,
    'height': 150,
    'color': 'orange',
    'shadow': 0.8
}

action_of_button = {
    'action': 'Buy',
    'text-info': 'Successful!'
}

# Merging all three dictionaries into one
ready_button = name_button | style_of_button | action_of_button
print(ready_button)
