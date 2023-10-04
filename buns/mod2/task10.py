words = input("Введите список слов через пробел: ")
current_word = ''
result = ''
for char in words:
    if char == ' ':
        if current_word:
            result += current_word[-1]
            current_word = ''
    else:
        current_word += char
if current_word:
    result += current_word[-1]
print("Результат:", result)