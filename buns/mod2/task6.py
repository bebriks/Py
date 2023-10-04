a = input("Введите доменное имя сайта:")
current_block = ''
reverse_blocks = ''
while True:
    if len(a) > 0:
        st = a[0]
        if st != '.':
            current_block += st
            a = a[1:]
        else:
            reverse_blocks = current_block + '\n' + reverse_blocks
            a = a[1:]
            current_block = ''
    else:
        reverse_blocks = current_block + '\n' + reverse_blocks
        break
print(reverse_blocks)