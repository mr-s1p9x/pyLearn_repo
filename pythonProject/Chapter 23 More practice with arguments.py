# Practice from teacher #

# Task 1
# 1. Переписать вызов функции merge_lists_to_dict из предыдущей задачи так,
# чтобы в нем использовались аргументы с ключевыми словами

def merge_lists_to_dict(list_one, list_two):
    return dict(zip(list_one, list_two))

# named arguments were added: list_one= list_two=
res_one = merge_lists_to_dict(list_one = ['a', 'b', 'c'], list_two = [10, True, []])
print(res_one)
# named arguments were added: list_two= list_one= | swapped, but result the same: {'abc': {}}
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