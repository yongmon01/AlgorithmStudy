INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # A->B : C
    a, b, c = map(int, input().split())
    if graph[a][b] != 0 and graph[a][b] < c:
        continue
    graph[a][b] = c

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 1e9:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
