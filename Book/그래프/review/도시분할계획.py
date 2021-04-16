import heapq
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
q = []

print(parent)

def find_parent(parent, p):
    if parent[p] != p:
        parent[p] = find_parent(parent, parent[p])
    return parent[p]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

answer, last = 0, 0
for i in range(m):
    a, b, c = heapq.heappop(q)
    if find_parent(parent, b) != find_parent(parent, c):
        answer += a
        last = a
        union_parent(parent, b, c)
print(answer - last)

# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4