from pydantic import validate_arguments


@validate_arguments
def psp(n: int) -> str:
    """
    Описание:
    Функция возвращает все скобочные последовательности в лексикографическом порядке при n открвающих скобках
    """
    def next_sequence(sequence: str) -> str:
        """
        Описание:
        Функция принимает на вход скобочную последовательность, возвращает следующую скобочную последовательность, в
        соответствии с лексикографическим порядком, если скобочная последовательность являлась последней, функция
        вернет 'No next sequence'
        """
        count_opened = 0
        count_closed = 0
        for bracket in reversed(sequence):
            if bracket == ')':
                count_closed += 1
            else:
                count_opened += 1
                if count_opened < count_closed:
                    break
        sequence = sequence[:len(sequence)-count_closed-count_opened]
        if not sequence:
            return 'No next sequence'
        sequence += ')'
        for i in range(count_opened):
            sequence += '('
        for i in range(count_closed-1):
            sequence += ')'
        return sequence

    result = ''
    sequence = '(' * n + ')' * n
    while sequence != 'No next sequence':
        result += sequence + '\n'
        sequence = next_sequence(sequence)
    return result.rstrip()

