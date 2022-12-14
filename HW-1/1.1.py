def nearest_zero(array: str) -> str:
    array = list(map(int, array.split()))
    result = array.copy()  # все элементы в нем мы изменим, нужен просто список такой же длины
    current_distance = None
    for i in range(len(array)):
        if array[i] and current_distance is not None:
            current_distance += 1
        elif not array[i]:
            current_distance = 0
        result[i] = current_distance

    current_distance = None
    for i in reversed(range(len(array))):
        if array[i] and current_distance is not None:
            current_distance += 1
        elif not array[i]:
            current_distance = 0
        if current_distance and ((result[i] is None) or (current_distance < result[i])):
            result[i] = current_distance
    result = list(map(str, result))
    return ' '.join(result)

print(nearest_zero('0 1 4 9 0'))
# 0 1 2 1 0
print(nearest_zero('0 7 9 4 8 20'))
# 0 1 2 3 4 5
print(nearest_zero('1 5 0 7 9 4 8 20 0 2 3 6 10 0 11 12'))
# 2 1 0 1 2 3 2 1 0 1 2 2 1 0 1 2