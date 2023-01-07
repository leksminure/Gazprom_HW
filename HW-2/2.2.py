from functools import reduce
from pydantic import validate_arguments


@validate_arguments
def largest_number(n: int, numbers: str) -> str:
    """
    Описание:
    В функции совершается проход по всем числам из входной строки и для каждого считается сумма
    Далее формируется список кортежей из числа и его суммы и сортируется по второму элементу, то есть его сумме
    Как итог происходит конкатенация всех чисел, являющихся строками и первыми элементами кортежей

    Параметры
    ----------
    n : число чисел, содержащихся во входной строке
    numbers: строка с n числами, записанными через пробел. Каждое отдельное число не превосходит 1000
    ----------
    Возвращаемые значения
    ----------
    result: строка, являющаяся конкатенацией и максимальным числом при данных входныхых числах
    """
    def sum_of_digits(number: int):
        """
        Описание:
        Функция принимает на вход число, возвращает сумму его отдельно взятых цифр
        """
        result = 0
        while number != 0:
            last_digit = number % 10
            result += last_digit
            number //= 10
        return result

    if n == 0:
        return ''
    numbers_sums = []
    numbers = numbers.split()
    for i in range(n):
        numbers_sums.append(
            (numbers[i], sum_of_digits(int(numbers[i])))
        )
    numbers_sums = sorted(numbers_sums, key=lambda x: x[1], reverse=True)
    numbers = [x[0] for x in numbers_sums]
    result = reduce(lambda x, y: x+y, numbers)
    return result