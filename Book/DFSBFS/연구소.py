# 내답 실행시간 3초 답지 실행시간 15초
import time
from itertools import combinations

start = time.time()
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,1,-1]

temp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        temp[i][j] = graph[i][j]

answer = 0

def count_safe(graph):
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 0:
                count += 1
    return count

def virus(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                virus(graph, nx, ny)

def gogo(graph):
    global answer
    global temp
    zero_list = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                zero_list.append((i, j))
    com_list = list(combinations(zero_list, 3))
    print(com_list)
    for i in com_list:
        for j in i:
            temp[j[0]][j[1]] = 1
        for p in range(n):
            for q in range(m):
                if temp[p][q] == 2:
                    virus(temp,p,q)
        answer = max(answer, count_safe(temp))
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]



# def gogo(graph, count):
#     global answer
#     if count == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = graph[i][j]
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(temp,i,j)
#         answer = max(answer, count_safe(temp))
#         return
#     for p in range(n):
#         for q in range(m):
#             if graph[p][q] == 0:
#                 graph[p][q] = 1
#                 count += 1
#                 gogo(graph, count)
#                 graph[p][q] = 0
#                 count -= 1

gogo(graph)
print(answer)
print("time :", time.time() - start)

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0