phone_number = input("Введите номер телефона: ")
print(''.join(char for char in phone_number if char.isdigit() or char == '+'))