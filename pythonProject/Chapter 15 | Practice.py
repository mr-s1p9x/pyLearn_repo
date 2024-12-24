# Задача 1
# 1. Создайте список с 5 элементов разных типов
# 2. Удалите третий элемент
# 3. Выведите в терминал длину списка
# 4. Поменяйте порядок следования элементов в списке
# 5. Создайте еще один список с двумя элементами
# 6. Расширьте первый список элементами второго списка
# 7. Выведите в терминал расширенный список из 6 элементов

# ==== 1 =====
my_list = [5, 2.3, 'hi', True, [3, 4, 5]]
print(my_list) # printing our list

# ==== 2 =====
my_list.pop(3) # removing the third element

# ==== 3 ====
print(len(my_list)) # printing length of list

# ==== 4 ====
# Method 1
print(my_list[::-1]) # or my_list.reverse()
# Method 2
my_list.reverse()
# print(my_list) # reversed list

# ==== 5 ====
# extending lists
my_list_2 = [2, 4.324]

# ==== 6 ====
# Method 1
my_list.extend(my_list_2)

# ==== 7 ====
print(f'Using .extend ===> {my_list}')
print(len(my_list))
# Method 2
# extended_list = my_list + my_list_2
# print(extended_list)

print("========================================")
# Задача 2
# 1. Создайте два списка
# 2. Объедините два списка, используя оператор +
# 3. Определите, какой магический метод списков вызывается при использовании оператора +
# 4. Выполните слияние списков, используя этот магический метод
# 5. Результат выведите в терминал
# ==== 1 ====
list_1 = [1, 3, 4.2, 'hi']

# ==== 2 ====
list_2 = ['python', 3, 234.23, True]

# ==== 3 ====
list_3 = list_1 + list_2
print(list_3)

# ==== 4 ====
magic_result = list_1.__add__(list_2)
# compare each other, if True then method __add__ is using for +
print(list_3 == magic_result)
print(magic_result) # for 4 and 5 step

