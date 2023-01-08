from pydantic import validate_arguments


@validate_arguments
def convert_to_bin(number: int) -> str:
    """
    Функция переводящая целые числа из десятичной системы исчисления в двоичную
    :param number: Входное целое число в десятичной системе исчисления
    :return: Число переведенное в двоичную систему исчисления
    """
    if number == 0:
        return '0'
    result = []
    is_negative = number < 0
    number = abs(number) if is_negative else number
    while number != 0:
        remainder = number % 2
        result.append(str(remainder))
        number //= 2
    result = ''.join(reversed(result))
    return result if not is_negative else '-'+result


for i in range(-999999, 999999):
    assert convert_to_bin(i) == bin(i)[2:] if i > 0 else bin(i)[0] + bin(i)[3:]
