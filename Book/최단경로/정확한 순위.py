# # 이렇게 bfs로 풀어봤는데 이것도 맞는것같아
#
# from collections import deque
# n, m = map(int, input().split())
#
# graph = [[] for _ in range(n+1)]
# for i in range(1, n+1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# path_list = [[]]
# visited = [False] * (n+1)
# answer = 0
#
# def bfs(node):
#     path = []
#     queue = deque()
#     queue.append(node)
#     visited[node] = True
#     while queue:
#         next_node = queue.popleft()
#         path.append(next_node)
#         for nod in graph[next_node]:
#             if visited[nod] is False:
#                 queue.append(nod)
#                 visited[nod] = True
#     for i in range(1, n+1):
#         visited[i] = False
#     return path
#
# for i in range(1, n+1):
#     current = bfs(i)
#     print(i, current)
#     path_list.append(current)
#
# print(path_list)
#
# for i in range(1, n+1):
#     add = True
#     current_list = path_list[i]
#     for j in range(1, n +1):
#         if i in path_list[j] or j in current_list:
#             continue
#         else:
#             add = False
#     if add is True:
#         answer += 1
#
# print(answer)


INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b  = map(int, input().split())
    graph[a][b] = 1

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):

            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("x", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()

# 6
# 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4


# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4