from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления ' +
           'квадратного корня из заданного числа.')

def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)

def calc(your_number):
    """Выполняет проверку аргумента."""
#    print (f'Вы ввели число {your_number}.')
    if your_number < 0:
        print(f'Невозможно извечь квадратный корень из отрицательного числа. ' 
              f'Это операция, обратная возведению в степень 2.')
    elif your_number == 0:
        print(f'Квадратный корень из 0 = 0')
    else:
        root = calculate_square_root(your_number)
        return print(f'Мы вычислили корень квадратный '
                     f'из введенного вами числа. '
                     f'Это будет: {root}')

print(message)
calc (25.5)