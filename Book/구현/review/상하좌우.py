n = int(input())

moves = list(input().split())
print(moves)
x, y = 0, 0

for move in moves:
    dx, dy = 0, 0
    if move == 'L':
        dy = -1
    elif move == 'R':
        dy = 1
    elif move == 'U':
        dx = -1
    elif move == 'D':
        dx = 1
    nx = x + dx
    ny = y + dy
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
        x = nx
        y = ny
print(x+1, y+1)

# 5
# R R R U D D