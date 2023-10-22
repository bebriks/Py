def step_number(number, step):
    if step == 0:
        return 1
    elif step % 2 == 0:
        temp = step_number(number, step // 2)
        return temp * temp
    else:
        temp = step_number(number, step - 1)
        return number * temp
res = step_number(int(input("Введите число:")), int(input("Введите степень:")))
print(res)
