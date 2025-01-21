#### immutable objects in function ####
def my_fn(a, b):
    a = a + 1 # new object created
    c = a + b
    return c

num_one = 10
num_two = 5

res = my_fn(num_one, num_two)
print(res)
print(num_one) # didn't change


#### mutable objects in function ####
def increase_person_age(person):
    person['age'] += 1
    print(id(person)) # same id with person_one
    return person

person_one = {
    'name': 'Bob',
    'age': 21
}

print(id(person_one)) # gonna be the same id as in function
increase_person_age(person_one)
print(person_one['age'])

# Задача не тест
# 1. Создать функцию merge_lists_to_dict
# 2. У функции должно быть два параметра
# 3. Функция должна объединять два списка, используя встроенную функцию zip
# 4. Конвертируйте объект zip в словарь и верните его из функции
# 5. Вызовите функцию, передав ей два списка в качестве аргументов
def merge_lists_to_dict(list1, list2):
    zip_list = zip(list1, list2)
    dict_list = dict(zip_list)
    return dict_list

# short form
# def merge_lists_do_dict(list1, list2):
#     return dict(zip(list1, list2))

consoles = ['xbox', 'playstation', 'nintendo']
prices = [450, 500, 350]

print(merge_lists_to_dict(consoles, prices))



