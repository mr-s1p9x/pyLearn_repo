my_name = 'Artem'
my_hobby = 'drawing'
time = 8

info = my_name + ' likes ' + my_hobby + ' at ' + str(time) + ' o\'clock'
print(info)

# using f-strings
info = f"{my_name} likes {my_hobby} at {str(time)} o'clock"
# 1. Capitalize every word in string
print(info.title()) # .title() method

# 2. Create 4 different variable and use f-sting to print them
name = 'Artem'
series = range(1, 6)
temp = 5.4
checking = True

info_2 = f"""It was cold, temperature was around {str(temp)}C 
and {name} standed on the street and counted {' '.join(str(i) for i in series)}. 
Is it {str(checking)}?"""
print(info_2)
