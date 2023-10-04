side = float(input("Введите сторону квадрата:"))
p = 4 * side
s = side ** 2
diagonal = (2 * side**2) ** 0.5
print('{:.2f}, {:.2f}, {:.2f}'.format(p, s, diagonal))