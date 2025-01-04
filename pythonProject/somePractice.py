print("==== 7 ====")
# Раздел 7: Введение в функции
#
#     Напишите функцию, которая принимает два числа и возвращает их сумму.
def twoNums(a, b):
    return a + b
print(twoNums(5, 10))

#     Создайте функцию, которая определяет, является ли переданное число чётным.
def even_odd(num):
    if num %2 == 0:
        print("Num is even")
    else:
        print("Num is odd")
even_odd(2)

#     Напишите функцию, которая принимает строку и возвращает её перевёрнутую версию.
def reverseString(word):
    return word[::-1]
print(reverseString("Hello"))

#####################################################################################
print("==== 8 ====")
# Раздел 8: Выражения и инструкции
#
#     Используя условный оператор if, проверьте, является ли число положительным,
#     отрицательным или нулём.
def numCheck(num):
    if num > 0:
        print("Num is positive")
    elif num == 0:
        print("Num is 0")
    else:
        print("Num is negative")
numCheck(10)

#     Реализуйте цикл for, который выводит все числа от 1 до 10.
for n in range(1, 11):
    print(n, end=" ")
    n += 1
print()

#     Используя while, создайте простой счётчик, который останавливается
#     при достижении значения 5.
count = 0
while count != 5:
    print(count, end=" ")
    count += 1
print()

print("==== 9 ====")
# Раздел 9: Переменные
#
#     Объявите три переменные: строку, число и булево значение. Выведите их на экран.
num = 1
name = "Artem"
isTrue = True
print(num, name, isTrue)

#     Поменяйте местами значения двух переменных без использования третьей переменной.
a, b = 5, 10
print(a, b)
a, b = 10, 5
print(a, b)

#     Создайте переменную со значением в 100 и увеличьте её вдвое.
num = 100
print(num * 2)

print("==== 10 ====")
# Раздел 10: Типы и структуры данных
#
#     Создайте список, в который поместите строку, число и логическое значение.
myList = ['hi', 100, True]
print(type(myList))

# Определите тип любого объекта (например, числа) с помощью функции type().
print(type(myList[0]))
print(type(myList[1]))
print(type(myList[2]))

#     Проверьте, является ли заданный объект списком, используя функцию isinstance.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = isinstance(nums, list)
print(res)

print("==== 11 ====")
# Раздел 11: Строки
#
#     Напишите программу, которая берёт строку и выводит её в верхнем регистре.
# myString = input("Enter something: ")
# print(myString.upper())
#
# #     Разбейте строку на отдельные слова с помощью метода .split().
# newString = []
# print(myString[1])
#
# for n in range(len(myString)):
#     newString += myString[n].split(' ,')
# print(newString)


#     Проверьте, заканчивается ли строка символом !.
# myString_2 = input("Enter something: ")
# maxIndex = len(myString_2)
#
# if myString_2[maxIndex - 1] == '!':
#     print(True)
# else:
#     print(False)

print("==== 12 ====")
# Раздел 12: Целые и другие числа в Python
#
#     Напишите программу, которая делит два числа и выводит остаток.
print(17 % 5)
#     Создайте переменную с дробным числом. Преобразуйте его в целое число
#     с помощью функции int().
num1 = 5.2
print(int(num1))

#     Найдите среднее арифметическое трёх чисел.
nums_1 = [3, 45, 21, 1, 4, 32, 12]

sum = 0
for n in range(len(nums_1)):
    sum += nums_1[n]
arithmeticMean = sum / len(nums_1)
print(arithmeticMean)

print("==== 13 ====")

# Раздел 13: Логический тип
#
#     Проверьте, является ли длина строки больше 5, используя логическое выражение.
# myStringCheck = input("Enter something")
# if len(myStringCheck) >= 5:
#     print(True)
# else:
#     print(False)

#     Создайте выражение, которое возвращает True, если число делится на 3.
number = 9
if number % 3 == 0:
    print(True)
else:
    print(False)

print("----")
#     Напишите программу, которая проверяет, содержится ли заданный элемент в списке.
listOfElemets = [10, 'hi', True, 1029, 282.3, 'python']
searchElement = 282.3
resultFound = 0

for n in range(len(listOfElemets)):
    if listOfElemets[n] == searchElement:
        resultFound = listOfElemets[n]

if resultFound == 0:
    resultFound = False

print(f'result exists: {resultFound}')

print("==== 14 ====")
# Раздел 14: Магические методы
#
#     Создайте класс с магическим методом __str__, который возвращает строку
#     "Объект создан!".
# creating class with magic method __str__
class magicExample:
    def __str__(self):
        return f'Object created!'
    #     Реализуйте класс с методом __len__, который возвращает фиксированное число
    #     (например, 42).
    def __len__(self):
        return 42

#     Напишите класс с методом __eq__, который сравнивает два объекта по их атрибуту.
class MyObject:
    def __init__(self, attribute):
        self.attribute = attribute

    def __eq__(self, other):
        if isinstance(other, MyObject):
            return self.attribute == other.attribute
        return False

# Creating an instance of the class
run = magicExample()
# printing our string
print(run) # uses __str__
print(len(run)) # uses __len__

obj1 = MyObject(10)
obj2 = MyObject(10)
obj3 = MyObject(20)

print(obj1 == obj2)
print(obj1 == obj3)

print("==== 15 ====")
# Раздел 15: Списки
#
#     Создайте список из 5 чисел. Удалите второй элемент.
listFive = [1, 2, 3, 4, 5]
print(listFive)
del listFive[2]
print(listFive)

#     Добавьте новый элемент в конец списка с помощью метода .append().
listFive.append(10)
print(listFive)

#     Объедините два списка с помощью оператора +.
listSix = [5, 29, 190]
listSeven = listFive + listSix
print(listSeven)

print("==== 16 ====")
# Раздел 16: Словари
#
#     Создайте словарь, где ключами будут названия стран, а значениями — их столицы.
countries = {'Italy': 'Milan', 'USA': 'Washington', 'France': 'Paris'}
print(type(countries))
print(countries)

#     Удалите один из ключей из словаря.
del countries['France']
print(countries)

#     Напишите программу, которая выводит только ключи словаря.
print(countries.keys())

print("==== 17 ====")
# Раздел 17: Кортежи
#
#     Создайте кортеж из трёх элементов. Попробуйте изменить один из них. Что произойдёт?
myTuple = ('type-a', 'type-b', 'type-c')
print(type(myTuple))
# we CANNOT chagne tuples, it will raise an error

#     Преобразуйте кортеж в список, добавьте элемент, а затем снова преобразуйте в кортеж.
listConvert = list(myTuple)
print(type(listConvert))
listConvert.append('type-d')
myTuple = tuple(listConvert)
print(myTuple)

#     Найдите индекс заданного элемента в кортеже.
# Its gonna be last index, .append method adding element in the end of the list
print(len(myTuple))
print(myTuple[3])

print("==== 18 ====")
# Раздел 18: Наборы
#
#     Создайте два множества и найдите их разницу.
fruits_1 = {'banana', 'apple', 'lime', 'grape'}
fruits_2 = {'apple', 'lime', 'guava', 'peach'}
print(fruits_1.difference(fruits_2)) # fruits_2 doesn't contain banana and grape
print(fruits_2.difference(fruits_1)) # fruits_1 doesn't contain guava and peach

#     Проверьте, является ли одно множество подмножеством другого.
print(fruits_1.issubset(fruits_2)) # False
print(fruits_2.issubset(fruits_1)) # False

#     Напишите программу, которая удаляет все элементы из множества.
fruits_1.clear()
fruits_2.clear()
print(fruits_1, fruits_2) # set() set()

print("==== 19 ====")
# Раздел 19: Диапазоны
#
#     Создайте диапазон чисел от 1 до 10 и выведите их в виде списка.
myRange = range(1, 11)
for n in myRange:
    print(n, end=" ")
    n += 1
print()
#     Напишите программу, которая проверяет, входит ли число 7 в диапазон от 5 до 15.
rangeCheck = range(5, 16)
check = 7

for n in rangeCheck:
    if n == check:
       print(True)

#     Найдите сумму всех чисел в диапазоне от 1 до 100.
sumRange = range(1, 101)
sum = 0
for n in sumRange:
    sum += n
    n += 1

print(sum)

print("==== 20 ====")
# Раздел 20: Функция zip
#
#     Создайте два списка (имена и возраста) и объедините их с помощью zip.
names = ['John', 'James', 'Will', 'Mike', 'Ben']
ages = [30, 24, 16, 40, 54]
combinedZip = zip(names, ages) # zip won't display it, so we need to convert in list also
combinedList = list(combinedZip)
print(combinedList)

#     Преобразуйте результат zip в список кортежей.
#combinedTuple = tuple(combinedZip)
#print(combinedTuple)

#     Распакуйте zip-объект обратно в два отдельных списка.
print('Unzipped:')
unzipped_names, unzipped_ages = zip(*combinedList) # unzipping
# converting into lists back
names_restored = list(unzipped_names)
ages_restored = list(unzipped_ages)

print(names_restored)
print(ages_restored)