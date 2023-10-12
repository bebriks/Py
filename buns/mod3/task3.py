domain = input("Введите доменное имя сайта:")
print(*domain.split('.')[::-1], sep='\n')