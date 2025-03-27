# 1. Создайте функцию route_info, которой будет передаваться словарь

# 2. Если в словаре есть ключ distance и его значение - целое число, верните строку
# "Distance to your destinationt is <distance>"

# 3. Иначе, если в словаре есть ключи speed и time, верните строку
# "Distance to your destination is <speed> * <time>"
# Можно также сделать проверку, что скорость целое число и время также

# 4. Иначе верните строку "No distance info is available"

# 5. Вызовите функцию несколько раз с разными аргументами


def route_info(**kwargs):
    distance = kwargs.get('distance')
    speed = kwargs.get('speed')
    time = kwargs.get('time')

    if isinstance(distance, int):
        return f"Distance to your destination is {distance} km"

    if (speed is not None and not isinstance(speed, int)) or \
       (time is not None and not isinstance(time, int)):
        return "One of the arguments is not INT"

    if speed is not None and time is not None:
        return f"Distance to your destination is {speed * time} km"

    return "No distance info is available"


# Тесты
print(route_info(distance=10))               # ✔ Distance to your destination is 10 km
print(route_info(speed=50, time=3))          # ✔ Distance to your destination is 150 km
print(route_info())                          # ✔ No distance info is available
print(route_info(speed="fast", time=3))      # ✔ One of the arguments is not INT
print(route_info(distance=0))                # ✔ Distance to your destination is 0 km

    

