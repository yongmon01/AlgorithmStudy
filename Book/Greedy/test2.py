from collections import deque
# 도시개수, 도로개수, 거리, 출발
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
length = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)
queue = deque([x])
count = 1
length[x] = 0
visited[x] = True
while queue:
    p = queue.popleft()
    for i in graph[p]:
        if visited[i] is False:
            visited[i] = True
            length[i] = length[p] + 1
            queue.append(i)

print(length)

if k not in length:
    print(-1)
else:
    for i in range(len(length)):
        if length[i] == k:
            print(i)
