# 도시개수, 도로개수, 거리, 출발
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

answer = graph[x]
for a in answer:
    visited[a] = True
print('graph',graph)
print('visited',visited)
print('answer',answer)
for i in range(k-1):
    print(answer)
    new_answer = []
    for a in answer:
        for f in graph[a]:
            if visited[f] is False:
                new_answer.append(f)
                visited[f] = True
    answer = []
    for a in new_answer:
        answer.append(a)
answer.sort()
if len(answer) == 0:
    print(-1)
else:
    for a in answer:
        print(a)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4