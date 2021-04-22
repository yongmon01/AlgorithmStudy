from itertools import combinations
from copy import deepcopy

yes = False
n = int(input())
graph = []
students, teachers, empty = [], [], []
for i in range(n):
    graph.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            students.append((i, j))
        elif graph[i][j] == 'T':
            teachers.append((i, j))
        else:
            empty.append((i, j))

# print(graph)
# print(students)
# print(teachers)
# print(empty)
wall = list(combinations(empty, 3))
# print('wall', wall)

def hide(n, graph, teachers):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in teachers:
        x, y = i[0], i[1]
        for j in range(4):
            nx, ny = x, y
            while nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] != 'O':
                if graph[nx][ny] == 'S':
                    return False
                nx += dx[j]
                ny += dy[j]
    return True

for i in range(len(wall)):
    test_graph = deepcopy(graph)
    for j in wall[i]:
        x, y = j[0], j[1]
        test_graph[x][y] = 'O'
    if hide(n, test_graph, teachers):
        print(test_graph)
        yes = True

if yes:
    print('YES')
else:
    print('NO')

# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X