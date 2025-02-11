from copy import deepcopy
# 1. Создайте две переменные и присвойте им одинаковые последовательности типа set.
# При этом не копируйте одну переменную в другую.
   
fruit_set_1 = {'apple', 'banana'}
fruit_set_2 = deepcopy(fruit_set_1)

# checking 
print(hex(id(fruit_set_1)))
print(hex(id(fruit_set_2)))
  
# 2. Выведите в терминал результат сравнения двух созданныъ объектов, объясните результат
print(fruit_set_1 == fruit_set_2) # True


# 3. Сравните два объекта используйте оператор is, объясните результат
print(fruit_set_1 is fruit_set_2)

# 4. Проверьте, есть ли определенные элементы в наборе, используя in
print(fruit_set_1.issuperset(fruit_set_2)) # True
print(fruit_set_1.issubset(fruit_set_2)) # True


    