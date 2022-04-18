from typing import Callable, Union

CallFloat= Callable[[Union[int, float]], float]

def add(number: Union[int, float], callback: CallFloat) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """    
    return callback(number)


def adder20(number: Union[int, float]) -> float:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: Union[int, float]) -> float:
    """Умножает аргумент на 2."""
    return number * 2
example = 5.5
res=add(example, multiplier2)

print (adder20(example))
print (multiplier2(example))
print (res)