# casual func
# def mult(a, b):
#     return a * b

# lambda func
# lambda a, b: a * b

# practice 
def greeting(greet):
    return lambda name: f"{greet}, {name}!"

morning_greeting = greeting("Good morning")
print(morning_greeting("Artem"))
# Good morning, Artem!

evening_greeting = greeting("Good evening")
print(evening_greeting("Artem"))

day = greeting("-Today is a good weather. Isn't it?")
print(day("\n-Oh, yeah! The sun is shining"))