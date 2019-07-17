custom_list = ['some', 1, 'v', 40, '3a', str]

new_list = list(filter(lambda x: type(x) != str, custom_list))

print(new_list)