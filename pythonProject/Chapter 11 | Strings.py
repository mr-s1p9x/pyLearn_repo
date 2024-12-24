# Структура и синтаксис строки
my_name = "Artem"
print(my_name)
# Artem

long_str = "This is very long string"
print(long_str)
print(type(long_str)) # <class 'str'>

multi_string = """ 
This is 
multiline
string
:)
"""
print(multi_string)

# Найти длину строки
print(len(my_name)) # 5

# Отображение определенного символа строки по индексу
print(my_name[1]) # r

# Отображение диапазона, от и до, например:
print(my_name[1:4]) # Первый индекс - включительно, а второй - нет

# Some practice
my_comment = "This is my short comment"
print(len(my_comment))

print(my_comment.replace("short", "long")) # что меняем / на что меняем
print(my_comment)

# Symbols count
print(my_comment.count('s')) # 3

print(my_comment[-5]) # 5th symbol from end