# 1. Создайте функцию image_info с одним параметром типа dict

# 2. Функция ожидает словарь, в котором должно быть как минимум два ключа:
# - image_id
# - image_title 

# 3. Функция должна возвращать строку такого вида "Image 'my_cat' has id 5136"
def image_info(lib_images):
    # 4. Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку
    # TypeError
    if 'image_id' not in lib_images or 'image_title' not in lib_images:
        raise TypeError("Dictionary must contain 'image_id' and 'image_title'!")

    return f"Image '{lib_images['image_title']}' has id {lib_images['image_id']}"

image_id = 5136
image_title = 'my_cat'

lib_images = {
    'image_id': image_id,
    'image_title': image_title
}

# 5. Вызовите функцию и корректно обработайте ошибку в случае возникновения
try:
    print(image_info(lib_images))
except TypeError as e:
    print(f"Error: {e}")





