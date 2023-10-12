def check_winner(field, k):
    # Проверка горизонтальных комбинаций
    for row in field:
        if 'X' * k in row: return 'X'
        elif 'O' * k in row: return 'O'
    # Проверка вертикальных комбинаций
    for col in range(len(field[0])):
        column = ''.join([field[row][col] for row in range(len(field))])
        if 'X' * k in column: return 'X'
        elif 'O' * k in column: return 'O'
    # Проверка главной диагонали
    diagonal = ''.join([field[i][i] for i in range(len(field))])
    if 'X' * k in diagonal: return 'X'
    elif 'O' * k in diagonal: return 'O'
    # Проверка побочной диагонали
    diagonal = ''.join([field[i][len(field) - i - 1] for i in range(len(field))])
    if 'X' * k in diagonal: return 'X'
    elif 'O' * k in diagonal: return 'O'
    return 'Ничья'
field = []
while True:
    try:
        row = input()
        if not row: break
        field.append(row)
    except EOFError: break
winner = check_winner(field, len(field))
print(winner)
