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
print(route_info(distance=10))               # Distance to your destination is 10 km
print(route_info(speed=50, time=3))          # Distance to your destination is 150 km
print(route_info())                          # No distance info is available
print(route_info(speed="fast", time=3))      # One of the arguments is not INT
print(route_info(distance=0))                # Distance to your destination is 0 km
print()

##################################################
# Teacher's version
def route_info_new(route):
    # Check if 'distance' key exists and is of type int
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']} km" 
    
    # Check if both 'speed' and 'time' keys exist and are integers\
    if ('speed' in route and 'time' in route) and \
    (type(route['speed']) == int) and (type(route['time']) == int):
        return f"Distance to your destination is {route['speed'] * route['time']} km"

    # If none of the above, return default message
    return "No distance info is available"

print(route_info_new({'distance': 15}))
print(route_info_new({'speed': 50, 'time': 3}))
print(route_info_new({'my_speed': 20}))
print()

## IF ELIF ELSE examples
# Function that returns distance info based on keys in a dictionary

def route_info_new_2(route):
    if ('distance' in route) and (type(route['distance']) == int):
        info = f"Distance to your destination is {route['distance']} km" 
    
    elif ('speed' in route and 'time' in route) and \
    (type(route['speed']) == int) and (type(route['time']) == int):
        info =  f"Distance to your destination is {route['speed'] * route['time']} km"

    else: 
        info = "No distance info is available"

    return info

print(route_info_new_2({'distance': 25}))
print(route_info_new_2({'speed': 30, 'time': 2}))
print(route_info_new_2({'my_speed': 40}))


