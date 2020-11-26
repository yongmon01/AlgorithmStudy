from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
# 도시개수 도로개수 거리 출발지점

long = [-1] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

queue = deque()
queue.append(x)
long[x] = 0
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if long[i] == -1:
            long[i] = long[v] + 1
            queue.append(i)
#print('long: ',long)

printed = False
for i in range(len(long)):
    if long[i] == k:
        print(i)
        printed = True
if printed == False:
    print(-1)
# 4 4 3 1
# 1 2
# 1 3
# 2 3
# 2 4