# 1. Создайте две переменные и присвойте им одинаковые последовательности типа set.
# При этом не копируйте одну переменную в другую.

# different objects, located in difference memory addresses
# but the same objects in both
fruit_set_1 = {'apple', 'banana', True, 10}
fruit_set_2 = {'apple', 'banana', True, 10}
  
# 2. Выведите в терминал результат сравнения двух созданныъ объектов, объясните результат
print("\nCompare them: ")
print(fruit_set_1 == fruit_set_2) # True

# Let's check the magic method
print(fruit_set_1.__eq__(fruit_set_2)) # True

# 3. Сравните два объекта используйте оператор is, объясните результат
print("\nComparing using 'is':")
print(fruit_set_1 is fruit_set_2) # False | they have different pointers to different objects in mem
# But if we chage set_2 = set_1 we'll get True
fruit_set_2 = fruit_set_1
print(fruit_set_1 is fruit_set_2) # True | now both point to the same object in memory

# Even if we mix the same objects in set, we will get the same results as above
# for example if
# set_1 = {'apple', True, 'banana', 10}
# set_2 = {'apple, 'banana', True, 10}
# for Python it's gonna be equal object, but those objects are different, 
# because both point to the different addresses in memory

print()
# 4. Проверьте, есть ли определенные элементы в наборе, используя in
print('apple' in fruit_set_1) # True 
print('apple' in fruit_set_2) # True
print(1000 in fruit_set_1)  # False
#print([] in fruit_set_1) # TypeError: unhashable type: 'list'

# False value examples
# we can use built in fuction bool() to doublecheck
print(bool(0))
print(bool(0.0))
print(bool(0j))
print()

print(bool({}))
print(bool([]))
print(bool(()))
print(bool(set()))
print(bool(range(0)))
print(bool(""))
print()

print(bool(False))
print(bool(None))
print()

# we can also use double 'not'
print(not not {})
print()

# some more practice
print(not not {'a': 10})
print(not not ['abc', 10, 20])
print(not not 1)
print(not not 1.2)
print(not not 0j)
print(not not 8j)
print(not not {True, False, 10, 'abc'})
print(not not range(0, 10))
print(not not range(1, 11))
print(not not "word")