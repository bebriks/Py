def get_armstrong():
    while(True):
        for i in range(100, 100_000):
            arm_number = 0
            for el in str(i):
                arm_number += int(el)**len(str(i))
            if i == arm_number:
                yield arm_number

gen = get_armstrong()

def get_armstrong_numbers():
    return next(gen)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')
