
from collections import deque

n, m, k, x = map(int, input().split())
# 도시개수 도로개수 거리 출발지점

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

queue = deque()
visited[x] = True
queue.append(x)
for i in range(k):
    print(i, '***************')
    length = len(queue)
    if length != 0:
        for j in range(length):
            v = queue.popleft()
            print(v, ' is popped')
            for q in graph[v]:
                if visited[q] is False:
                    visited[q] = True
                    queue.append(q)
                    print(q, ' is appended')
if len(queue) == 0:
    print(-1)
else:
    for g in queue:
        print('%',g,'%')

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 4 3 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 3 2 1
# 1 2
# 1 3
# 1 4



# # 아니 이건 대체왜 아니지 답이???
# from collections import deque
#
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# distance = [0] * (n+1)
#
# def bfs(graph, v):
#     queue = deque()
#     queue.append(v)
#     for i in range(k):
#         length = len(queue)
#         if length == 0:
#             print(-1)
#             return
#         for j in range(length):
#             current = queue.popleft()
#             d = distance[current]
#             for q in graph[current]:
#                 if distance[q] == 0:
#                     queue.append(q)
#                     distance[q] = d + 1
#     if len(queue) == 0:
#         print(-1)
#         return
#     for i in queue:
#         print(i)
#
# bfs(graph, x)
# # print(distance)







# from collections import deque
#
# def dfs(graph, v, z):
#     queue = deque()
#     visited[v] = True
#     queue.append(v)
#     for i in range(z):
#         print(i, '***************')
#         length = len(queue)
#         # if length == 0:
#         #     print(-1)
#         #     break
#         for j in range(length):
#             v = queue.popleft()
#             print(v, ' is popped')
#             for q in graph[v]:
#                 if visited[q] is False:
#                     visited[q] = True
#                     queue.append(q)
#                     print(q, ' is appended')
#     if len(queue) == 0:
#         print(-1)
#     else:
#         for g in queue:
#             print('%',g,'%')
#
# n, m, k, x = map(int, input().split())
# # 도시개수 도로개수 거리 출발지점
#
# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# print(graph)
#
# dfs(graph, x, k)
#
# # 4 4 2 1
# # 1 2
# # 1 3
# # 2 3
# # 2 4
#
# # 4 4 1 1
# # 1 2
# # 1 3
# # 2 3
# # 2 4








# from collections import deque
# import sys
#
# input = sys.stdin.readline
# n, m, k, x = map(int, input().split())
# # 도시개수 도로개수 거리 출발지점
#
# long = [-1] * (n+1)
# graph = [[] for _ in range(n+1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# queue = deque()
# queue.append(x)
# long[x] = 0
# while queue:
#     v = queue.popleft()
#     for i in graph[v]:
#         if long[i] == -1:
#             long[i] = long[v] + 1
#             queue.append(i)
# #print('long: ',long)
#
# printed = False
# for i in range(len(long)):
#     if long[i] == k:
#         print(i)
#         printed = True
# if printed == False:
#     print(-1)
