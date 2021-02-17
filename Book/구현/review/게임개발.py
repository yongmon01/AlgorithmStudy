n, m = map(int, input().split())
x, y, direction = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
direct = [0,1,2,3]
# 위 오 아래 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

print(graph)
count = 0
while True:
    # 왼쪽 회전
    direction = direction - 1
    if direction == -1:
        direction = 3
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 갈수있다면
    if nx >=0 and ny >= 0 and nx < m and ny < n and graph[nx][ny] == 0:
        x, y = nx, ny
        graph[x][y] = 2
        count = 0
        continue
    print('갈수있다', x,y,direction)
    # 갈수없다면
    count += 1
    if count < 4:
        print('갈수없다', x, y, direction)
        continue

    # 뒤로 한칸
    nx = x + dx[(direction+2) % 4]
    ny = y + dy[(direction+2) % 4]
    # 뒤로갈수없다면
    if nx < 0 or ny < 0 or nx >= m or ny >= n or graph[nx][ny] == 1:
        print('뒤로못간다', nx, ny, direction)
        break
    # 가능하다면
    x, y = nx, ny
    graph[nx][ny] = 2
    print('뒤로간다', x, y, direction)
    count = 0

print(graph)


# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1