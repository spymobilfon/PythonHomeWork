# Clear list
multiple_7 = []
not_multiple_7 = []

# Cycle check multiple 7
for number in range(1, 100 + 1):
    if number % 7 == 0:
        multiple_7.append(number)
    else:
        not_multiple_7.append(number)

# Print result
print("Числа кратные 7:\n", multiple_7)
print("Числа не кратные 7:\n", not_multiple_7)