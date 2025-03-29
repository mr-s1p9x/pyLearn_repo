my_img = ('1920', '1080')

print(my_img) if (
    len(my_img) == 2
    and isinstance(my_img[0], str)
    and isinstance(my_img[1], str)
) else print('No exaсt resolution')


# Practice
# 1. Rewrite using if else
if len(my_img) == 2 and (isinstance(my_img[0], str) and isinstance(my_img[1], str)):
    print(my_img)
else:
    print('No exaсt resolution')

# 2. If string > 79 print 'string is long' else 'string is short'
my_word = '231234230423723442389fsdfisdbnfidfsfiusfg32434fgervertbtrb5499hdegg9jg945g045g45'

print('string is long') if len(my_word) > 79 else print('string is short')