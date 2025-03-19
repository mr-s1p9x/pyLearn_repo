# Список словарей, в нем будет 3 словаря, далее с помощ оператора распаковки списков
# созд 3 переменных, каждая из которых будет содерж 1 из словарей
# далее функция которая будет принимать 2 аргумента и в вызове функции будет распаковка словаря
# функцию нужно вызвать трижды, т.к ориг словая 3 и у каждого должно быть по 2 ключа

# 1. Создаём список из трёх словарей, каждый содержит информацию о пользователе
list_of_dict = [
    {"name": "Alice", "comments_qty": 24},
    {"name": "Dan", "comments_qty": 29},
    {"name": "Sofia", "comments_qty": 38}
]

# 2. Распаковываем список в три отдельные переменные
dict_1, dict_2, dict_3 = list_of_dict

# 3. Функция принимает два аргумента (имя и количество комментариев)
# и возвращает строку с информацией. Если одного из аргументов нет – вызывает ошибку.
def show_info(name, comments_qty=None):
    if comments_qty is None or name is None:
        raise TypeError("One of required arguments is missing or empty: name, comments_qty")
    return f"{name} has {comments_qty} comments"

# 4. Вызываем функцию трижды, передавая в неё данные через распаковку словарей
for d in (dict_1, dict_2, dict_3):
    try:
        print(show_info(**d))
    except TypeError as e:
        print(e)
