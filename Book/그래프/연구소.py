# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# temp = [[0]*m for _ in range(n)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# count = 0
#
# def dfs(x, y):
#     if x <= 0 or x >= n or y <= 0 or y >= m:
#         return
#     if temp[x][y] == 0:
#         temp[x][y] = 2
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)
#
# for i in range(n):
#     for j in range(m):
#         if
#
#
