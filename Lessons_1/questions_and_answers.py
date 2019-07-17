# Clear the value of variables
correct_answer = 0
not_correct_answer = 0

# Set the value options for YES and NO
value_yes = ["yes", "true", "да", "верно", "правда"]
value_no = ["no", "false", "нет", "не верно", "ложь"]

# Block of the questions and answers

answer_1 = input("Какой это язык программирования?\nОтвет: ")

if answer_1.lower() == "python":
    print("Правильный ответ!")
    correct_answer += 1
else:
    print("Не правильный ответ :(")
    not_correct_answer += 1

answer_2 = input("5 больше 10?\nОтвет: ")

if answer_2.lower() in value_no:
    print("Правильный ответ!")
    correct_answer += 1
else:
    print("Не правильный ответ :(")
    not_correct_answer += 1

answer_3 = input("10 больше 5?\nОтвет: ")

if answer_3.lower() in value_yes:
    print("Правильный ответ!")
    correct_answer += 1
else:
    print("Не правильный ответ :(")
    not_correct_answer += 1

answer_4 = input("4 делится на 2?\nОтвет: ")

if answer_4.lower() in value_yes:
    print("Правильный ответ!")
    correct_answer += 1
else:
    print("Не правильный ответ :(")
    not_correct_answer += 1

answer_5 = input("Сколько будет 5 умножить на 2?\nОтвет: ")

try:
    answer_5_integer = int(answer_5)
except ValueError:
    print("Не правильный ответ :(")
    not_correct_answer += 1
else:
    if answer_5_integer == 10:
        print("Правильный ответ!")
        correct_answer += 1
    else:
        print("Не правильный ответ :(")
        not_correct_answer += 1

# Print result
print("Общее количество вопросов {}.\nПравильных ответов {}.\nНе правильных ответов {}.".format(correct_answer + not_correct_answer, correct_answer, not_correct_answer))