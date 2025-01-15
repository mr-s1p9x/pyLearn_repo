# Раздел 5: Встроенные функции в Python
# 1. Работа с dir и print:
# Создай переменную, например, строку "Hello World", и используй функцию dir,
# чтобы вывести все атрибуты строки.
# Затем выведи объяснение каждого метода, который начинается с буквы "i".

# my_str = "Hello World"
# attributes = dir(my_str)
# print(attributes)
# for attr in attributes:
#     if attr.startswith("i"):
#         print(f"{attr}: {getattr(my_str, attr).__doc__}")

# 2. Методы строк:
# Напиши функцию, которая принимает строку и возвращает
# её перевёрнутую версию, но с заглавными буквами.

# my_str2 = "Hello World"
# def reverse_string(my_str2):
#     return my_str2[::-1]
# print(reverse_string(my_str2.upper()))


# 3. Ввод данных:
# Напиши программу, которая спрашивает у пользователя имя, возраст и любимый цвет,
# а затем выводит сообщение:
# "Привет, <имя>. Тебе <возраст> лет, и твой любимый цвет — <цвет>!".
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# favourite_color = input("Enter your favorite color: ")
# print(f"Hi, {name}. You are {age} y.o, and your favorite color - {favourite_color}!")



# Раздел 6: Форматирование кода и PEP8
# 1. Форматирование с помощью black или autopep8:
# Возьми кусок кода, написанный без форматирования
# (например, без отступов и с длинными строками),
# и отформатируй его вручную, а потом с помощью автоформатирования.



# 2. Комментарии:
# Напиши программу, которая вычисляет площадь прямоугольника.
# Добавь комментарии, объясняющие каждую строку кода.

# print("This program calculates square of rectangle")
# # Добавляем int для того, чтобы привести строку к числу
# # Иначе нам просто посчитает строки и выведет числа в строку
# a = int(input("Enter a: "))                  # сторона а
# b = int(input("Enter b: "))                  # сторона b
# square = (a + b) * 2                         # формула для подсчета
# print(f"Rectangle's square is {square} cm2") # вывод площади



# ====================================================================
# Раздел 7: Введение в функции
# 1. Объявление функции:
# Напиши функцию, которая принимает список чисел и возвращает их среднее значение.

# num_list = [5, 3, 2, 1, 9]      # список элементов
# def middle_arif(numbers):       # функция подсчетя среднего ариф
#     sum = 0                     # счетчик суммы
#     count = 0                   # счетчик кол-ва элементов
#     for i in numbers:           # проходимся циклом по кол-ву элементов
#         sum += i                # плюсуем каждый i-ый элемент
#         count += 1              # считаем кол-во элементов
#     return sum / count          # возвращаем сумму / кол-во элементов
#
# print(middle_arif(num_list))    # выводим среднее арифметическое



# 2. Работа с return:
# Напиши функцию, которая принимает два числа и возвращает их сумму и разность.

# a = int(input("Enter first digit: "))
# b = int(input("Enter second digit: "))
#
# def sum_sub(a, b):
#     sum = a + b
#     sub = a - b
#     return sum, sub
#
# print(sum_sub(a, b))



# 3. Итоговая задача по функциям:
# Напиши функцию, которая принимает список строк и возвращает список длин
# каждой строки.

# mystr_list = ["hello", "world", "python"] # list of words
# def str_len(strings):                     # function
#     new_str_list = []                     # creating new list (for calculation)
#     for i in strings:                     # going through the list
#         new_str_list.append(len(i))       # using .append method for adding length for each string
#     return new_str_list                   # new list returning
#
# print(str_len(mystr_list))                # printing final results



# ====================================================================
# Раздел 8: Выражения и инструкции
# 1. Условные выражения:
# Напиши программу, которая спрашивает у пользователя число и выводит
# "Четное", если число делится на 2, и "Нечетное", если нет.

# print("This programm defines is number even either odd")
# number = int(input("Please enter a number: "))
# if number %2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")



# 2. Циклы:
# Напиши цикл, который выводит квадраты чисел от 1 до 10.
# numbers = 20
# for i in range(1, 21):
#     print(i)



# ====================================================================
# Раздел 9: Переменные
# 1. Объявление переменных:
# Напиши программу, которая хранит список покупок, добавляет в него три продукта,
# удаляет один, а затем выводит итоговый список.

# product_list = []
# product_list.append("apple")
# product_list.append("milk")
# product_list.append("cheese")
# product_list.append("water")
# print(product_list)
# product_list.remove("cheese")
# print(product_list)



# 2. Работа с несколькими переменными:
# Создай три переменные: a, b и c. Присвой им значения 5, 10 и 15.
# Напиши программу, которая меняет их местами так, чтобы a = 15, b = 5, и c = 10.
a, b, c = 5, 10, 15
a, b, c = c, a, b
print(a, b, c)



