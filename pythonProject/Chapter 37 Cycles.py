# Looping through a mixed list
for item in [1, 'abc', True]:
    print(type(item))
    print(item)

# 'item' is still available outside the loop and holds the last value
print(item)  # True

# We can also see it in the current namespace
print(dir())

# ⚠️ Tip: avoid reusing variable names if they were defined earlier


# --- Dictionary example ---
my_dict = {
    'id': 324,
    'title': 'art'
}

# Looping through keys
for key in my_dict:
    print(type(key))
    print(key, my_dict[key])

print()

# Looping with .items() and unpacking manually
for item in my_dict.items():
    key, value = item
    print(key, value)

print()

# Cleaner way — direct tuple unpacking
for key, value in my_dict.items():
    print(key, value)

print()

# --- Set example ---
video_ids = {1435, 4317, 2739, 5403}

for video_id in video_ids:
    print(video_id)

print()

# --- Some practice with range ---
# Print numbers from 1 to 30
for num in range(1, 31):
    print(num, end=' ')

print()

# Print every 5th number from 1 to 100
for step in range(1, 100, 5):
    print(step, end=' ')
