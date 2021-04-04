# nxn
n = int(input())

matrix = [[0]*(n+1) for _ in range(n+1)]
matrix[1][1] = 2
# 사과개수
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a][b] = 1

# 방향전환 개수
l = int(input())
turn = []
for _ in range(l):
    a, b = input().split()
    turn.append((int(a), b))

print(matrix)
print(turn)

# 오 아래 좌 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# D +1, L -1
def return_direction(num, dl):
    if dl == "L":
        num = (num - 1) % 4
    else:
        num = (num + 1) % 4
    return num

snake_x = [1]
snake_y = [1]

time, d, dead = 1, 0, False
while True:
    print(time)

    # 사과있냐
    prev_x = snake_x[-1]
    prev_y = snake_y[-1]

    # 대가리 한칸 갔을때(가정) 대가리가 몸통에 닫으면 죽음
    for i in range(1, len(snake_x)):
        if snake_x[0] + dx[d] == snake_x[i] and snake_y[0] + dy[d] == snake_y[i]:
            print(time)
            dead = True
            break
    if dead is True:
        break

    if len(snake_x) >= 2:
        for i in range(len(snake_x)-1):
            snake_x[len(snake_x)-i-1] = snake_x[len(snake_x)-i-2]
            snake_y[len(snake_y)-i-1] = snake_y[len(snake_y)-i-2]

    # 대가리 움직
    snake_x[0] += dx[d]
    snake_y[0] += dy[d]

    # 방향에 따라 d 값정하고
    if turn:
        if turn[0][0] == time:
            d = return_direction(d, turn[0][1])
            del turn[0]

    print(matrix)
    print(snake_x)
    print(snake_y)

    if snake_x[0] < 1 or snake_x[0] > n or snake_y[0] < 1 or snake_y[0] > n:
        print(time)
        break

    # 대가리가 사과닿으면 꼬리추가
    if matrix[snake_x[0]][snake_y[0]] == 1:
        snake_x.append(prev_x)
        snake_y.append(prev_y)
        matrix[snake_x[0]][snake_y[0]] = 0

    time += 1

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L