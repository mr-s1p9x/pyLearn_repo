# Practice from teacher #

# Task 1
# 1. Переписать вызов функции merge_lists_to_dict из предыдущей задачи так,
# чтобы в нем использовались аргументы с ключевыми словами

def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))

# named arguments were added: list_one= list_two=
# the order is not important
res_one = merge_lists_to_dict(list_one = ['a', 'b', 'c'], list_two = [10, True, []])
print(res_one)

# named arguments were added: list_two= list_one= | swapped, but result the same: {'abc': {}}
# the order is not important
res_two = merge_lists_to_dict(list_two = [{}, True, 100], list_one = ['abc']) # rest will be ignored
print(res_two)

# 2. Добавить еще один вызов функции, в котором будет один позиционный аргумент,
# а второй - аргумент с ключевым словом
# To avoid an error we must provide a named argument to the smallest list
# 1st list has 3 object, 2nd - only one, so 'a' -> 'abc' and rest will be ignored
res_three = merge_lists_to_dict(['a', True, 100], list_two = ['abc']) # rest will be ignored
print(res_three)

# Error - SyntaxError: positional argument follows keyword argument
# res_three = merge_lists_to_dict(list_two = ['a', True, 100], ['abc']) # rest will be ignored
# print(res_three)

##########################

# Task 2 
# 1. Создать функцию update_car_info, в которой все именованные аргументы будут объединяться 
# в словарь car
def update_car_info(**car):
    # 2. Добавить в словарь новый ключ is_awailable с значением True
    car['is_available'] = True
    # 3. Вернуть из функции измененный словарь
    return car
# 4. Вызвать функцию с именованными аргументами brand и price, их значения могут быть любыми
car = update_car_info(brand = "Honda", price = 20000)
print(car)

# TypeError: update_car_info() takes 0 positional arguments but 2 were given
# car = update_car_info("Honda", 20000)
# print(car)
