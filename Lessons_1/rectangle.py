# Clear the value of variables
side_a = 0
side_b = 0

# Input length side A
while True:
    side_a = input("Введите длину стороны A: ")
    try:
        side_a_float = float(side_a)
        break
    except ValueError:
        print("Значение должно быть числом. Попробуйте еще раз.")

# Input length side B
while True:
    side_b = input("Введите длину стороны B: ")
    try:
        side_b_float = float(side_b)
        break
    except ValueError:
        print("Значение должно быть числом. Попробуйте еще раз.")

# Print result
print("Площадь прямоугольника равна ", side_a_float * side_b_float)