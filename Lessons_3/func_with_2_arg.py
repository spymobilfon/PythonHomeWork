# Set function
def two_arg(first_arg, second_arg):
    if (first_arg > 0 and second_arg > 0):
        return first_arg + second_arg
    if (first_arg < 0 and second_arg < 0):
        return first_arg - second_arg
    if ((first_arg > 0 and second_arg < 0) or (first_arg < 0 and second_arg > 0)):
        return 0

# Enter arguments
user_input_first = input("Введите аргумент номер один:\n")
user_input_second = input("Введите аргумент номер два:\n")

# Check arguments
try:
    user_first_arg = int(user_input_first)
    user_second_arg = int(user_input_second)
except ValueError:
    print("Аргумент должен быть числом")
else:
    print("Получается:", two_arg(user_first_arg, user_second_arg))