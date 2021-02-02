import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
print(graph)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0

possible = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            possible.append((i, j))
# print(possible)

possible_list = list(combinations(possible, 3))
print(possible_list)

def count_safe(graph):
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                count += 1
    return count

def virus(graphh, x, y):

    graphh[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and graphh[nx][ny] == 0:
            virus(graphh, nx, ny)

def copy_matrix(graph):
    new_graph = []
    for i in range(len(graph)):
        current = []
        for j in range(len(graph[i])):
            current.append(graph[i][j])
        new_graph.append(current)
    return new_graph

for i in range(len(possible_list)):
    copied = copy_matrix(graph)
    for j in possible_list[i]:
        copied[j[0]][j[1]] = 1
    for p in range(len(copied)):
        for q in range(len(copied[p])):
            if copied[p][q] == 2:
                virus(copied, p, q)
    # print(copied)
    answer = max(answer, count_safe(copied))



print(answer)




# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2