def check_barcode(barcode):
    if len(barcode) != 13: return 'no'
    odd_digits = [int(barcode[i]) for i in range(0, 13, 2)]
    even_digits = [int(barcode[i]) for i in range(1, 12, 2)]
    if (sum(odd_digits) + sum(even_digits) * 3) % 10 == 0: return 'yes'
    else: return 'no'
barcode = input("Введите штрих-код: ")
result = check_barcode(barcode)
print(result)