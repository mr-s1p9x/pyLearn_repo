# Динамическая типизация в Python
def print_name(name):
    print(name)

print_name("Artem") # Artem

print_name = 15

# print_name("Artem") # TypeError: 'int' object is not callable


my_name = "Artem"
print(id(my_name)) # print address in memory

my_num = 100
print((id(my_num))) # 138203436410376

other_num = my_num
print(id(other_num)) # the same addr as my_num
