# 1. Создайте пустой словарь
# 2. Трижды попросите пользователя сначала ввести название ключа,
# а потом ввести значение для этого ключа. Всего должно быть 6
# запросов на ввод текста
# 3. Во время получения данных от пользователя добавляйте в словарь ключи
# со значениями согласно тому, что ввел пользователь
# 4. Выведите результирующий словарь в терминал

empty_dict = {}
print('Hi! you will be prompted to enter keys and values for the dictionary')

###### SOLUTION 1 ######
# print('Please, enter key, and after enter value for that key')
#
# key1 = input('Please enter 1st key name for your value: ')
# value1 = input('Now enter value for key1: ')
#
# key2 = input('Please enter 2nd key name for your value: ')
# value2 = input('Now enter value for key2: ')
#
# key3 = input('Please enter 3rd key name for your value: ')
# value3 = input('Now enter value for key3: ')
#
# key4 = input('Please enter 4th key name for your value: ')
# value4 = input('Now enter value for key4: ')
#
# empty_dict[key1] = value1
# empty_dict[key2] = value2
# empty_dict[key3] = value3
# empty_dict[key4] = value4
#
# print(empty_dict)

###### SOLUTION 2 ######
## Or we can use for
total_records = int(input('Please enter amount of records you wanna insert: '))
count = 1

for i in range(total_records):
    key = input(f'Enter key {count}#: ')
    value = input(f'Enter value {count}#: ')
    count += 1
    empty_dict[key] = value

print(empty_dict)