def divide(number):
    return number % 5

int_list = [1, 4, 5, 30, 99]

new_list = list(map(divide, int_list))
print(new_list)