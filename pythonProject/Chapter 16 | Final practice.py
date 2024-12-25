# 2. Введение в функции
#
# Создайте функцию is_even, которая принимает число и возвращает True,
# если число чётное, и False, если нечётное.
def is_even(number):
    if number %2 == 0:
        print(True)
    else:
        print(False)
is_even(3)


# 3. Выражения и инструкции
#
# Напишите программу, которая принимает два числа от пользователя и:
#
#     Если первое число больше второго, выводит "Первое больше".
#     Если второе больше первого, выводит "Второе больше".
#     Если числа равны, выводит "Числа равны".

# ==== uncomment me!
#a = int(input('Please enter first digit: '))
#b = int(input('Please enter second digit: '))
# ==== uncomment me!
def constr_cal(a, b):
    if a > b:
        print('First digit is bigger!')
    elif a < b:
        print('Second digit is bigger!')
    else:
        print('Digits are equal')
# ==== uncomment me!
#constr_cal(a, b)
# ==== uncomment me!


# 4. Переменные
#
# Напишите программу, которая:
#
#     Запрашивает у пользователя его имя.
#     Запрашивает возраст.
#     Выводит: "Привет, {имя}, тебе {возраст} лет!".
# ==== uncomment me!
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print(f'Hello, {name}, you are {age} y.o!')
# ==== uncomment me!


# 5. Типы и структуры данных
#
# Создайте программу, которая:
#
#     Принимает от пользователя строку с числами, разделёнными пробелами
#     (например, "1 2 3 4").
#     Преобразует её в список целых чисел.
#     Выводит их сумму, минимальное и максимальное значение.
numbers_string = input('Please enter numbers, separated by space [1 2 3 ...]: ').split(' ')
# split method helps us to create a list from string
print(type(numbers_string), numbers_string) # checking it

integersNum = [] # creating an empty list
# going through every single element in list and convert it into int
for x in numbers_string:
    integersNum.append(int(x))
print(integersNum) # pringing it

count = 0 # creating count for the cycle
totalSum = 0 # creating variable for the sum

# going from 0 to length of integersNum list and sum each number
for i in range(len(integersNum)):
    totalSum += int(integersNum[i])
    count += 1
print(totalSum) # printing sum

# finding minimum and maximum
# creating standard start for start, 0 index
biggest = int(integersNum[0])
lowest = int(integersNum[0])

# using for for finding
for i in range(len(integersNum)):
    # find the biggest one every iteration, if found put into 'biggest'
    if int(integersNum[i]) > biggest:
        biggest = int(integersNum[i])
    # same here, but with lower value
    elif int(integersNum[i]) < lowest:
        lowest = int(integersNum[i])
print(biggest)
print(lowest)


# 6. Строки
#
# Напишите программу, которая:
#
#     Запрашивает у пользователя строку.
#     Преобразует строку:
#         Все буквы в верхний регистр.
#         Заменяет пробелы на символ _.
#     Выводит изменённую строку.
#
# 7. Целые и другие числа
#
# Напишите функцию calculate_percentage, которая принимает два числа: общее количество и количество элементов. Функция должна возвращать процент элементов от общего числа.
# 8. Логический тип
#
# Напишите программу, которая принимает возраст пользователя и проверяет:
#
#     Если возраст меньше 18, выводит "Доступ запрещён".
#     Если больше или равен 18, выводит "Доступ разрешён".
#
# 9. Магические методы
#
# Создайте класс Rectangle:
#
#     У класса должны быть свойства length и width.
#     Реализуйте метод __str__, который возвращает строку вида "Прямоугольник: длина={length}, ширина={width}".
#
# 10. Списки
#
# Напишите программу, которая:
#
#     Создаёт список из чисел от 1 до 10.
#     Умножает каждое число в списке на 2.
#     Выводит новый список.
#
# 11. Словари
#
# Создайте словарь, в котором ключами будут имена (строки), а значениями — возраст (числа). Напишите программу, которая:
#
#     Добавляет в словарь новые пары "имя-возраст".
#     Удаляет элемент по ключу.
#     Выводит итоговый словарь.