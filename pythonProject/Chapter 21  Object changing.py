######

my_number = 10
print(id(my_number)) # 125168704681200

other_number = 10
print(id(other_number)) # 125168704681200

print(id(10)) # 125168704681200

# Some practice
from copy import deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great course!')
info['reviews'].append('Super')

print(info_deepcopy)
print(info)


