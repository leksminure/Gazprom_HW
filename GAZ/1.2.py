def sleight_of_hand(k: int, field: str):
    field = list(map(list, field.split()))
    counts = {str(i): 0 for i in range(10)}
    counts.update({'.': 0})
    for i in range(len(field[0])):
        for j in range(len(field[0])):
            counts[field[i][j]] += 1
    k *= 2 # каждый на k клавиж может нажать
    result = 0
    for i in range(10):
        if counts[str(i)] and k >= counts[str(i)]:
            result += 1
    return result

print(sleight_of_hand(3, '11231\n12..2\n12..2\n12..2'))