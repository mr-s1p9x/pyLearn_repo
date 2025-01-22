# Пример функции
def hello(name):
    print("Hello there!", name, "!")

hello('Artem')

# Ключевое слово return в функциях
def sum_nums(a, b):
    sum = a + b
    return sum
    # Код после return выполняться не будет
    print("Line is not executed")

first_sum = sum_nums(10, 5)
print(first_sum)
second_sum = sum_nums(50.5, 30.1)
print(second_sum)

# Можно также передать саму функцию в функцию
# по сути первым аргументом а будет сама функция, которая сложит 50.5 + 31.3
# а вторым аргументом будет b - число 32.1
# как итог, внешняя функция sum_nums сложит 81.8 + 32.1
print(sum_nums(sum_nums(50.5, 31.3), 32.1))


