coordinate = input()

# ord
x = ord(coordinate[0]) - 96
y = int(coordinate[1])

possible_move_x = [-2,-2,-1,-1,1,1,2,2]
possible_move_y = [-1,1,-2,2,-2,2,-1,1]

count = 0

for i in range(len(possible_move_x)):
    new_x = x + possible_move_x[i]
    new_y = y + possible_move_y[i]
    if 0 < new_x < 9 and 0 < new_y < 9:
        count += 1

print(count)
