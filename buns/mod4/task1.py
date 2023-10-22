num = input("Введите числа через пробел:")
st_num = num.split(' ')
if len(set(st_num)) == 1:
    print("Все числа равны")
elif len(set(st_num)) == len(st_num):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")