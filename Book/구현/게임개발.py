#not solved yet

n, m = map(int, input().split())
x, y, face = map(int, input().split())

matrix = []
faces = [0, 1, 2, 3]
x_move = [0, -1, 0, 1]
y_move = [-1, 0, 1, 0]

for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

matrix[x][y] = 2

def turn_left():
    global face
    face = (face + 3) % 4

while True:
    moved = False
    for i in range(4):
        turn_left()

        if face == 0 and matrix[x][y-1] == 0:
            y -= 1
            matrix[x][y] = 2
            moved = True
        elif face == 1 and matrix[x+1][y] == 0:
            x += 1
            matrix[x][y] = 2
            moved = True
        elif face == 2 and matrix[x][y+1] == 0:
            y += 1
            matrix[x][y] = 2
            moved = True
        elif face == 3 and matrix[x-1][y] == 0:
            x -= 1
            matrix[x][y] = 2
            moved = True

    if not moved:
        if face == 0 and matrix[x][y + 1] != 1:
            y += 1
            matrix[x][y] = 2
            continue
        elif face == 1 and matrix[x - 1][y] != 1:
            x -= 1
            matrix[x][y] = 2
            continue
        elif face == 2 and matrix[x][y - 1] != 1:
            y -= 1
            matrix[x][y] = 2
            continue
        elif face == 3 and matrix[x + 1][y] != 1:
            x += 1
            matrix[x][y] = 2
            continue

    break

print(matrix)






