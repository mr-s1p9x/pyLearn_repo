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

# test

