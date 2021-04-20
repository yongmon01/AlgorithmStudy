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

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 1:
            graph[i+1].append(j+1)
path = list(map(int, input().split()))

parent = [i for i in range(n+1)]
print(graph)
for i in range(1, len(graph)):
    for j in range(len(graph[i])):
        print(i, graph[i][j])
        union_parent(parent, i, graph[i][j])

print(graph)
print(parent)
print(path)

answer = "YES"
for i in range(len(path)-1):
    if find_parent(parent, path[i]) != find_parent(parent, path[i+1]):
        answer = "NO"
        break
print(answer)
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

