### Lists practice ###

# example of dictionary list
my_videocards = [
    {
        'id': 830,
        'vendor': 'Asus',
        'model': 'GTX 1650'
    },
    {
        'id': 850,
        'vendor': 'MSI',
        'model': 'RTX 2070'
    },
    {
        'id': 930,
        'vendor': 'GIGABYTE',
        'model': 'RTX 3060'
    },
    {
        'id': 1030,
        'vendor': 'NVIDIA FE',
        'model': 'RTX 4080'
    }
]

print(my_videocards) # printing our videocards list
print(type(my_videocards)) # checking type
# some print practice
print(my_videocards[0])
print(my_videocards[2]['model'])
print(my_videocards[0:2]) # 2 not included

# add some videocards to our list
my_videocards.append({'id': 1090, 'vendor': 'PALIT', 'model': 'RTX 4060'})
my_videocards.append({'id': 1120, 'vendor': 'MSI', 'model': 'RTX 4090'})

print()
print("= An updated list =")
for position in my_videocards: # and print them
    print(position)

print(len(my_videocards))

print('===================================')
# Sorting example, using method .sort()
someIdList = [10, 239, 2432, 920, 30, 204, 123, 34, 50, 60, 30, 230, 304, 50]
print(f'unsorted list: {someIdList}')
someIdList.sort()
print(f'sorted list: {someIdList}')

print('===================================')
# this converts implies that only keys will be in the list
videoDict = {'vendor_1': 'Asus', 'vendor_2': 'Gigabyte', 'vendor_3': 'MSI'}
my_List = list(videoDict)
print(my_List)