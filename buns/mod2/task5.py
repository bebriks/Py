def shift_character(char, n):
    ascii_code = ord(char)
    offset = n % 26
    new_ascii_code = ascii_code + offset
    if char.islower() and new_ascii_code > ord('z'):
        new_ascii_code -= 26
    elif char.isupper() and new_ascii_code > ord('Z'):
        new_ascii_code -= 26
    new_char = chr(new_ascii_code)
    return new_char
char = input("Введите символ: ")
n = int(input("Введите смещение: "))
result = shift_character(char, n)
print(result)