# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
# print(parent)

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
        return parent[a]
    return a

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    x, y = map(int, input().split())
    if find_parent(x) == find_parent(y):
        print('nononono')
        break
    union_parent(x, y)

print(parent)
for i in range(len(parent)):
    print(find_parent(i), end = ' ')
print(parent)
