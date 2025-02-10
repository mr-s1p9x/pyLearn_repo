def print_number_info(num):
    if(num % 2) == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")

def print_square_num(num):
    print("Square of the num is", num * num)

def process_number(num, callback_fn):
    callback_fn(num)

entered_num = int(input("Enter any number: "))
process_number(entered_num, print_number_info)
process_number(entered_num, print_square_num)