numbers = input("Введите чсила через пробел:")
a = 0
b = 0
c = 0
sp_con = 0
lena = 0
lenb = 0
for char in numbers:
    if char ==' ':
        sp_con += 1
    if sp_con == 0:
        lena += 1
    if sp_con == 1:
        lenb += 1
a = numbers[:lena]
b = numbers[lena + 1:lena + lenb]
c = numbers[lenb + lena + 1]
if(a > b):
    if(c > a): print(a)
    elif(b < c): print(c)
    else:print(b)
elif(c > b):print(b)
else:
    if(c < a):print(a)
    else:print(c)