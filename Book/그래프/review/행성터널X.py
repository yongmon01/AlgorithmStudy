# 두점사이의 거리를 모두 따진다면 시간초과..
# 주어진 조건을 잘활용하자.. 주어진조건을 잘활용하면 시간복잡도를 확 줄일수있는 문제였다.

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

x, y, z = [], [], []

parent = [i for i in range(n+1)]
for i in range(n):
    a,b,c = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

print(x,y,z)

# graph = [[] for i in range(n+1)]
q = []
for i in range(n-1):
    heapq.heappush(q, (x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    heapq.heappush(q, (y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    heapq.heappush(q, (z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

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