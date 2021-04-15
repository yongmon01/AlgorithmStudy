n, m = map(int, input().split())
parent = [i for i in range(n+1)]

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
    x, y, z = map(int, input().split())
    if x == 0:
        union_parent(parent, y, z)
    elif x == 1:
        if find_parent(parent, y) == find_parent(parent, z):
            print('YES')
        else:
            print('NO')

