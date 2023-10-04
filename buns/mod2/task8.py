def count_chars_in_beginning(s, i):
    count = 0
    for char in s:
        if char == i:
            count += 1
        else:
            break
    return count
s = input("Введите строку: ")
i = input("Введите символ: ")
result = count_chars_in_beginning(s, i)
print(result)