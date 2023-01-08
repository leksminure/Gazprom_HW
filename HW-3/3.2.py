import re
from pydantic import validate_arguments


@validate_arguments
def is_palindrome(line: str) -> bool:
    """
    Функция проверяет является ли строка палиндромом
    :param line: Входная строка
    :return: True если строка является палиндромом, иначе False
    """
    processed_input = re.sub(r"[^\\dа-яА-Яa-zA-ZёЁ]", "", line.lower())
    mid_of_input = len(processed_input) // 2
    if len(processed_input) % 2 == 0:
        return True if processed_input[:mid_of_input] == processed_input[-1:mid_of_input-1:-1] else False
    else:
        return True if processed_input[:mid_of_input] == processed_input[-1:mid_of_input:-1] else False
