# Example 1 | Static
def mult_by_factor(value, multiplier = 1):
    return value * multiplier

print(mult_by_factor(10, 2))
print(mult_by_factor(10))

# Example 2 | Dynamic
from datetime import date

def get_week_day():
    # date.today() returns today's date, f.e. 2025-01-23
    # .strftime('%A') formats this date and returns full day, f.e. 'Thursday'
    return date.today().strftime('%A') 

# post - takes dict which contains info about post, weekday = default param 
def create_new_post(post, weekday = get_week_day()):
    post_copy = post.copy() # creating shallow copy, it won't change original
    post_copy['created_on_weekday'] = weekday
    return post_copy

initial_post = {
    'id': 243,
    'author': 'Artem'
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)