def calculate_robot_position(n):
    x, y = 0, 0
    dx, dy = 0, -1
    for i in range(1, n+1):
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            # изменение направления при смене "круга" спирали
            dx, dy = -dy, dx
        x += dx  # движение по x координате
        y += dy  # движение по y координате
    return -x, -y
with open('task9_input.txt', 'r') as file:
    N = int(file.readline().strip())
position = calculate_robot_position(N)
with open('task9_output.txt', 'w') as file:
    file.write(f"{position[0]} {position[1]}")