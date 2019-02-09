# Enter number
print('Введите число:')
user_number = int(input())

# Set exceptions
try:
    if user_number % 2 == 0:
        raise ValueError('Число четное')
    if user_number < 0:
        raise TypeError('Число меньше 0')
    if user_number > 10:
        raise IndexError('Число больше 10')
except ValueError:
    print('Число четное')
except TypeError:
    print('Число меньше 0')
except IndexError:
    print('Число больше 10')