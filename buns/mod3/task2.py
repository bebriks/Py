try: num = int(input("Введите число:")); f"{ print(f'{bin(num)[2:]}, {oct(num)[2:]}, {hex(num)[2:]}') if num > 0 else print('Неверный ввод')}"
except ValueError:print('Неверный ввод')