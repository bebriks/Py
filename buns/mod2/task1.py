numbers = input("Enter numeral or number:")
num1 = 0
num2 = 0
counter = 0
for char in numbers:
    if char in ',':
        num1 = int(numbers[:counter])
        num2 = int(numbers[counter + 2:])
    counter += 1
print(num1 % num2)