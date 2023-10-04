vowel = 0
consonant = 0
allowed_chars_vowel = 'ауоыиэяюёе'
allowed_chars_consonant = 'бвгджзйклмнпрстфхцчшщ'
sentence = input("Введите предложение:")
for char in sentence:
    if char in allowed_chars_vowel:
        vowel += 1
    elif char in allowed_chars_consonant:
        consonant += 1
print(f"{vowel}, {consonant}")