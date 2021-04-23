import heapq
import sys

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

input = sys.stdin.readline
n = int(input())
answer = 0
point = [0]
parent = [i for i in range(n+1)]
for i in range(n):
    a,b,c = map(int, input().split())
    point.append((a,b,c))

print(point)
graph = [[] for i in range(n+1)]
q = []

for i in range(1, n):
    for j in range(i+1, n+1):
        # graph[i].append(min(abs(point[i][0]-point[j][0]), abs(point[i][1]-point[j][1]), abs(point[i][2]-point[j][2])))
        # graph[j].append(min(abs(point[i][0]-point[j][0]), abs(point[i][1]-point[j][1]), abs(point[i][2]-point[j][2])))
        heapq.heappush(q, (min(abs(point[i][0]-point[j][0]), abs(point[i][1]-point[j][1]), abs(point[i][2]-point[j][2])),i,j))
print(q)
while q:
    l, a, b = heapq.heappop(q)
    if find_parent(parent,a) != find_parent(parent,b):
        answer += l
        union_parent(parent, a, b)


print(answer)

# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19