def sleight_of_hand(k: int, field: str) -> int:
    field = list(map(list, field.split()))
    counts = {str(i): 0 for i in range(1, 10)}
    counts.update({'.': 0})
    for i in range(len(field[0])):
        for j in range(len(field[0])):
            counts[field[i][j]] += 1
    k *= 2 # каждый на k клавиж может нажать
    result = 0
    for i in range(1, 10):
        if counts[str(i)] and k >= counts[str(i)]:
            result += 1
    return result

print(sleight_of_hand(3, '1231\n2..2\n2..2\n2..2'))
# output: 2
print(sleight_of_hand(4, '1111\n9999\n1111\n9911'))
# output: 1
print(sleight_of_hand(4, '1111\n1111\n1111\n1111'))
# output: 0
print(sleight_of_hand(2, '....\n....\n....\n....'))
# output: 0
print(sleight_of_hand(5, '1234\n5678\n9876\n5432'))
# output: 9