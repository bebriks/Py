def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)
res = euclid(int(input("Введите первое число:")), int(input("Введите второе число:")))
print(res)