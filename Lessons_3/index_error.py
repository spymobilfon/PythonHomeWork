# Set random list
random_list = [ 'alpha', 'beta', 'omega', 'ariel', 'zero', 'calibre', 'humor' ]

# Enter index
print('Введите индекс объекта:')
user_input = input()

try:
    user_index = int(user_input)
except ValueError:
    print("Индекс должен быть целым числом")
else:
    try:
        print(random_list[user_index])
    except IndexError:
        print("Объекта с таким индексом нет")