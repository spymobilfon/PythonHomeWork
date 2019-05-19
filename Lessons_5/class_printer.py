class Printer(object):
    def log(self, *values):
        print(values)

class FormattedPrinter(Printer):
    def log(self, *values):
        print('*'*(len(values)*3+2))
        print('*{}*'.format(values))
        print('*'*(len(values)*3+2))

numbers = Printer()
numbers.log(1, 2, 3, 4, 5, 6, 7, 8, 9)

stars_numbers = FormattedPrinter()
stars_numbers.log(1, 2, 3, 4, 5, 6, 7, 8, 9)