def clean_phone_number(phone_number):
    allowed_chars = '0123456789+'
    cleaned_number = ''.join(char for char in phone_number if char in allowed_chars)
    return cleaned_number
input_phone_number = input("Введите номер телефона: ")
cleaned_phone_number = clean_phone_number(input_phone_number)
print(cleaned_phone_number)