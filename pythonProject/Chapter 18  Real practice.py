# Task 1
# 1. Создайте набор из нескольких элементов типа int
nums_1 = {1, 2, 3, 5, 10, 12, 20, 34, 49}
# 2. Добавьте в него еще один элемент
nums_1.add(109)
# 3. Создайте еще один набор с несколькими элементами, причем некоторые
# должны быть такими же как в первом наборе
nums_2 = {5, 10, 12, 39, 23, 43, 49, 100}
# 4. Найдите общие элементы в двух наборах и поместите их в новый набор
common_nums = nums_1.intersection(nums_2)
print(common_nums)
# 5. Конвертируйте результирующий набор в список и выведите список в терминал
list_nums = list(common_nums)
print(list_nums)