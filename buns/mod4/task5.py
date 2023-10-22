with open('task5.txt', 'r') as file:
    text = file.read()
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    res_arr = sorted(counter.items(), key=lambda x: x[1])
with open('task5.txt', 'w') as file:
    for k,v in res_arr:
        file.write(f"{k}: {v}\n")