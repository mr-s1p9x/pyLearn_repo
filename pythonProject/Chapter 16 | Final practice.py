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
# def constr_cal(a, b):
#     if a > b:
#         print('First digit is bigger!')
#     elif a < b:
#         print('Second digit is bigger!')
#     else:
#         print('Digits are equal')
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
# ==== uncomment me!
# numbers_string = input('Please enter numbers, separated by space [1 2 3 ...]: ').split(' ')
# # split method helps us to create a list from string
# print(type(numbers_string), numbers_string) # checking it
#
# integersNum = [] # creating an empty list
# # going through every single element in list and convert it into int
# for x in numbers_string:
#     integersNum.append(int(x))
# print(integersNum) # pringing it
#
# count = 0 # creating count for the cycle
# totalSum = 0 # creating variable for the sum
#
# # going from 0 to length of integersNum list and sum each number
# for i in range(len(integersNum)):
#     totalSum += int(integersNum[i])
#     count += 1
# print(totalSum) # printing sum
#
# # finding minimum and maximum
# # creating standard start for start, 0 index
# biggest = int(integersNum[0])
# lowest = int(integersNum[0])
#
# # using for for finding
# for i in range(len(integersNum)):
#     # find the biggest one every iteration, if found put into 'biggest'
#     if int(integersNum[i]) > biggest:
#         biggest = int(integersNum[i])
#     # same here, but with lower value
#     elif int(integersNum[i]) < lowest:
#         lowest = int(integersNum[i])
# print(biggest)
# print(lowest)
# ==== uncomment me!

# 6. Строки
#
# Напишите программу, которая:
#
#     Запрашивает у пользователя строку.
#     Преобразует строку:
#         Все буквы в верхний регистр.
#         Заменяет пробелы на символ _.
#         Выводит изменённую строку.
# ==== uncomment me!
# some_word = input("Please enter some phrase: ")
# print(some_word.upper())
# print(some_word.replace(' ', '_'))
# ==== uncomment me!

# 7. Целые и другие числа
#
# Напишите функцию calculate_percentage, которая принимает два числа: общее количество
# и количество элементов. Функция должна возвращать процент элементов от общего числа.
# function for % calculation
def calculate_percentage(total, count):
    if total == 0: # escaping dividing by 0
        return 0
    percentage = (count / total) * 100 # default percentage calculation
    return percentage # returning %

total_items = 300
disks = 129
ramSticks = total_items - disks

# calling function to detect disks %
disks_percentage = calculate_percentage(total_items, disks)
# calling function to detect ram %
ram_percentage = calculate_percentage(total_items, ramSticks)

print(f'disks: {disks_percentage} %')
print(f'ram sticks:  {ram_percentage} %')

# 8. Логический тип
#
# Напишите программу, которая принимает возраст пользователя и проверяет:
#
#     Если возраст меньше 18, выводит "Доступ запрещён".
#     Если больше или равен 18, выводит "Доступ разрешён".
# age = int(input("Please enter your age: "))
# if age >= 18:
#     print("Access granted!")
# else:
#     print("Access denied.")


# 9. Магические методы
#
# Создайте класс Rectangle:
#
#     У класса должны быть свойства length и width.
#     Реализуйте метод __str__, который возвращает строку вида
#     "Прямоугольник: длина={length}, ширина={width}".
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return f'Rectangle square: {self.width * self.length}'

    def __str__(self):
        return f'Rectangle (length={self.length}, width={self.width})'

rect = Rectangle(10, 5)
print(rect)
print(rect.area())


# 10. Списки
#
# Напишите программу, которая:
#
#     Создаёт список из чисел от 1 до 10.
#     Умножает каждое число в списке на 2.
#     Выводит новый список.

# creating function
def numbersCreate():
    numList = [] # first empty list

    for i in range(1, 11): # going through the loop from 1 to 10
        numList.append(i) # appending 1, 2, 3 ... 10
    print(numList, type(numList)) # printing

    newNumList = [] # second empty list for multiplication
    for i in range(len(numList)): # same here, going through the length of list (10)
        newNumList.append(numList[i] * 2) # multiplication by 2 and appending
    print(newNumList, type(newNumList)) # printing
numbersCreate() # call our function

# 11. Словари
#
# Создайте словарь, в котором ключами будут имена (строки), а значениями — возраст (числа). Напишите программу, которая:
#
#     Добавляет в словарь новые пары "имя-возраст".
#     Удаляет элемент по ключу.
#     Выводит итоговый словарь.
print('This programm allow you to add peoples into list: Name - Age')
# amount of people we want to add
peopleAmount = int(input('Please enter amound of people you want to add: '))
peopleDict = {} # creating an empty dictionary

# Cycle for adding "name-age" pairs into dictionary
for i in range(peopleAmount):
    key = input("Please enter a name: ")
    value = int(input("Please enter age: "))
    peopleDict[key] = value

print(peopleDict) # printing

# name we want to delete
deleteName = input("Please enter person name you want to delete: ")

# casual checking
# if name exists - deleting it, if no - print "No such name, sorry"
if peopleDict.get(deleteName) == None:
    print("No such name, sorry")
else:
    peopleDict.pop(deleteName)
    print(f'Person with a name {deleteName} was deleted successfully')

print(peopleDict) # printing

