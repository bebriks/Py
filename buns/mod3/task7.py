num = input("Введите числа через пробел:").split(' ')
print(True if len(set(num)) < len(num) else False)
