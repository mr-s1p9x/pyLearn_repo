# chapter 7
# function returning 'hello, world!'
# def greeting():
#     print("Hello, World!")
# greeting()

# # sum function
# def sum_sum(a, b):
#     sum = a + b
#     return sum

# a = 10
# b = 5
# print(sum_sum(a, b))

# chapter 8
# printing some expressions
# print(20.5 + 30.31)

# name = "Artem"
# print(f'Hello, {name}!')

# text1 = "_Hello"
# text2 = "World_"
# print(f'{text1}, {text2}')

# chapter 9
# reverse string with upper
# my_word = input("Enter some phrase: ")

# def reverse_upper_string(word):
#     print(word.upper()[::-1])

# reverse_upper_string(my_word)

# some info about user
# u_name = input("Please enter your name: ")
# u_age = input("Please enter your age: ")
# fav_color = input("Please enter your favorite color: ")
# hobby = input("Please enter your hobby: ")

# print(f"Your name is {u_name}\nYou are {u_age} y.o\nYour favorite color is {fav_color} and your hobby is {hobby}")

##############################
# Раздел 7: Введение в функции
# 1. Напиши функцию, которая принимает два числа и возвращает их сумму
# num_1 = int(input("Enter num 1: "))
# num_2 = int(input("Enter num 2: "))

# def sum_nums(num_1, num_2):
#     sum = num_1 + num_2
#     return sum
# print(sum_nums(num_1, num_2))

# 2. Создай функцию, которая определяет, является ли число чётным.
# num = int(input("Enter number: "))

# if num % 2 == 0:
#     print("Num is even")
# elif num % 2 != 0:
#     print("Num is odd")
# else:
#     print("Unknown Error")

##############################
# Раздел 8: Выражения и инструкции
# 1. Используй условный оператор для проверки, больше ли первое число второго.
# num_11 = int(input("Enter first num: "))
# num_22 = int(input("Enter second num: "))

# if num_11 > num_22:
#     print(f"Num {num_11} > {num_22}")
# elif num_11 < num_22:
#     print(f"Num {num_11} < {num_22}")
# elif num_11 == num_22:
#     print(f"Num {num_11} = {num_22}")
# else:
#     print("Unknown error")

# 2. Напиши цикл for, который выводит числа от 1 до 10.
# for i in range(1, 11):
#     print(i, end=" ")

##############################
# Раздел 9: Переменные
# 1. Объяви три переменные: name (строка), age (число), is_student (логический тип). Выведи их на экран.
# name = "Artem"
# age = 26
# is_student = True
# print(name, age, is_student, sep=" | ")

# 2. Присвой переменной x значение 10, а затем увеличь его на 5.
# age += 5
# print(age)

##############################
# Раздел 10: Типы и структуры данных
# 1. Создай список с пятью элементами разных типов (например, строка, число, список). 
# Выведи тип каждого элемента.
# nickname = "H0wadrd_3000"
# lvl = 109
# skills = ['magic flame', 'armageddon', 'black arrow']

# print(type(nickname))
# print(type(lvl))
# print(type(skills))

# 2. Создай словарь, где ключами будут названия дней недели, а значениями — их порядковый номер.
# week_is = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
# print(week_is)

##############################
# Раздел 11: Строки
# 1. Напиши программу, которая принимает строку и возвращает её длину.
# some_word = input("Please enter some word: ")
# print(f"Length of your word is: {len(some_word)}")

# 2. Проверь, содержится ли в строке слово "Python". Если содержится, выведи сообщение "Найдено!".
# find_python = input("Enter some phrase: ")
# find_python = find_python.lower()

# if "python" in find_python:
#     print("Word 'python' exist in string")
# elif "python" not in find_python:
#     print("Word 'python' DOES NOT exist in string")
# else:
#     print("Unknown Error")

############################## 
# Раздел 12: Целые и другие числа в Python
# 1. Напиши функцию, которая принимает список чисел и возвращает их среднее значение.
# number_list = [10, 20, 28, 1, 3, 7, 23]

# def middle_num(num_list): 
#     sum = 0
#     for i in num_list:
#         sum += i
    
#     middle_arif = sum / len(num_list)
#     print(round(middle_arif, 2))

# middle_num(number_list)

# 2. Создай программу, которая преобразует число из десятичной системы в двоичную.
# decimalNum = int(input("Enter some number: "))

# def decimalToBinary(num):
#     if num >= 1:
#         decimalToBinary(num // 2)
#     print(num % 2, end = '')

# decimalToBinary(decimalNum)

# ##############################
# Раздел 13: Логический тип
# 1. Напиши программу, которая принимает два логических значения 
# и возвращает результат операции "И" (AND).
# a = True
# b = True

# def logAnd(a, b):
#     return a and b
# print(logAnd(a, b))

# 2. Проверь, является ли число чётным и положительным.
# someNum = 2
# if someNum % 2 == 0 and someNum > 0:
#     print(f"{someNum} is even and > 0")
# else:
#     print(f"{someNum} is odd or < 0")    

# ##############################
# Раздел 14: Магические методы
# 1. Создай класс Point с атрибутами x и y. Переопредели метод __str__, 
# чтобы он возвращал строку вида (x, y).
# 2. Добавь в класс Point метод __add__, который складывает координаты двух точек.
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
# point = Point(3, 5)
# print(Point)

# point1 = Point(2, 3)
# point2 = Point(4, 1)
# result = point1 + point2
# print(result)

# ##############################
# Раздел 15: Списки
# 1. Напиши программу, которая удаляет дубликаты из списка.
# 2. Отсортируй список чисел в порядке убывания
# someList = [10, 20, 3, 7, 3, 20, 11, 30, 44, 10]

# simple way
# def onlyUnique(list_dict):
#     uniquet_list = list(set(list_dict))
#     uniquet_list.sort(reverse = True)
#     return uniquet_list

# print(onlyUnique(someList))


# for / if way
# new_list = []
# for i in someList:
#     if i not in new_list:
#         new_list.append(i)

# new_list.sort(reverse = True)
# print(new_list)

# ##############################
# Раздел 16: Словари
# 1. Создай словарь, где ключами будут числа от 1 до 5, а значениями — их квадраты.
# powDict = {x: x ** 2 for x in range (1, 6)}
# print(powDict)

# 2. Напиши программу, которая находит значение по заданному ключу.
# foundKey = 3
# value = powDict.get(foundKey) # returning value or None, if key absent

# if value is not None:
#     print(f'Found: key={foundKey}, value={value}')
# else:
#     print(f'Key {foundKey} not found in the dictionary.')

# ##############################
# Раздел 17: Кортежи
# 1. Напиши функцию, которая принимает кортеж чисел и возвращает сумму его элементов.
# numTuple = (10, 20, 21, 5, 8, 38, 34, 22)

# def sumNum(num_sequence):
#     sum = 0
#     for i in num_sequence:
#         sum += i
#     return sum

# print(sumNum(numTuple))

# 2. Создай кортеж из трёх элементов, распакуй его в три переменные.
# consoles = ('playstataion', 'xbox', 'nintendo')
# a, b, c = consoles # literally means unpacking
# print(a)
# print(b)
# print(c)

# ##############################
# Раздел 18: Наборы
# 1. Напиши программу, которая находит пересечение двух множеств.
# file_formats = {'avi', 'mp4', 'mp3', 'flac', 'exe', 'txt', 'bin'}
# other_formats = {'mp4', 'flac', 'ini', 'docx', 'png', 'iso', 'exe'}
# common_formats = file_formats.intersection(other_formats)
# print(common_formats)

# 2. Создай множество, содержащее только уникальные элементы из списка.
# formats_list = ('avi', 'mp4', 'avi', 'exe', 'docx', 'png', 'iso', 'exe', 'ini', 'flac', 'avi', 'ini')
# formats_list_2 = ('mp4', 'flac', 'docx', 'png', 'iso', 'exe', 'flac', 'mp3', 'iso')
# new_formats = formats_list + formats_list_2
# only_unique_formats = set(new_formats)
# print(only_unique_formats)

# ##############################
# Раздел 19: Диапазоны
# 1. Напиши программу, которая выводит все чётные числа от 1 до 20 с использованием range().
for i in range(1, 21):
    print(i, end=" ")
print()
# 2. Создай список чисел от 10 до 1 в обратном порядке с помощью range().
for i in range(10, 0, -1):
    print(i, end=" ")