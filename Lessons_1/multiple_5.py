# Clear the value of variables
start_number = 0
stop_number = 0

# Input start number
while True:
    start_number = input("Введите начальное целое число: ")
    try:
        start_number_integer = int(start_number)
        break
    except ValueError:
        print("Значение должно быть целым числом. Попробуйте еще раз.")

# Input stop number
while True:
    stop_number = input("Введите конечное целое число: ")
    try:
        stop_number_integer = int(stop_number)
        break
    except ValueError:
        print("Значение должно быть целым числом. Попробуйте еще раз.")

# Clear the list
list_number = []

# Cycle check multiple 5
for n in range(start_number_integer, stop_number_integer + 1):
    if n % 5 == 0:
        list_number.append(n)

# Print result
print("Числа кратные 5:\n", list_number)