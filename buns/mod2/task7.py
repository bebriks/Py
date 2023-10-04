one = 0
zero = 0
bin_code = input("Введите бинарный код:")
allowed_symbols = '01'
for char in bin_code:
    if char in str(1) in allowed_symbols:
        one +=1
    if char in str(0) in allowed_symbols:
        zero +=1
print(f"{one}, {zero}")
if(one == zero): print("yes")
else: print("no")