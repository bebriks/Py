num = int(input("Введите размер матрицы:"))
matrix = []
for el in range(num): matrix.append([i for i  in range(1, num + 1)])
for part in matrix: print(", ".join(str(x) for x in part));
print('\n')
tr_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for part in tr_matrix: print(", ".join(str(x) for x in part))