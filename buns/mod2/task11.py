def check_rep():
    numbers = input("Введите числа: ")
    new_nums = ""
    for num in numbers:
        if num in new_nums:
            return True
        new_nums += num
    return False
print(check_rep())
