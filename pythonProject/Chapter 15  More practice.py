# Раздел 7: Введение в функции
#
#     Напишите функцию, которая принимает список чисел и возвращает их сумму.
def sum_nums(num_1, num_2, num_3, num_4, num_5):
    sum = num_1 + num_2 + num_3 + num_4 + num_5
    return sum

sum = sum_nums(3, 10.2, 304, 29, 10)
print(f'Sum of all numbers equals: {sum}')

#     Создайте функцию, проверяющую, является ли переданное число чётным.
def odd_or_even(digit):
    if digit %2 == 0:
        print(f'{digit} is even')
    else:
        print(f'{digit} is odd')
odd_or_even(32)

###########################################################################

# Раздел 10: Типы и структуры данных
#
#     Напишите функцию, которая принимает строку и возвращает словарь,
#     где ключ — слово, а значение — количество его вхождений.
my_str = "Python in all over the world for programmers"

def str_to_list(my_str):
    new_list = list(my_str)
    return {word: new_list.count(word) for word in new_list}
print(str_to_list(my_str))

#     Создайте функцию, которая возвращает множество общих элементов двух списков.
lst_1 = [1, 2, 4.32, True, 90]
lst_2 = [2, 3, 4.92, False, 10, 90]

def common_values(lst_1, lst_2):
    result = []
    for item in lst_1: # going through the list, every item-step in lst_1
        # so if item in lst_1 AND item in lst_2 not in result = add it into result
        if item in lst_2 and item not in result:
            result.append(item)
    return result
print(common_values(lst_1, lst_2))

###########################################################################

# Раздел 11: Строки
#
#     Создайте функцию, которая принимает строку и возвращает её в обратном порядке.
word_str = "Hello, Python!"
def reverse_string(string):
    return string[::-1]
print(reverse_string(word_str))

#     Напишите функцию, проверяющую, является ли строка палиндромом
#     (читается одинаково слева направо и справа налево).
word_str_2 = "ATATA"
def palindrome_check(string):
    if string == string[::-1]:
        print("Yor string is palindrome")
    else:
        print("Your string is NOT palindrome")
palindrome_check(word_str_2)