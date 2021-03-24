# 내풀이.. 멋있다.

n = int(input())
li = list(map(int, input().split()))
dp = [1] * n
graph = [[] for _ in range(n)]
graph[0].append(li[0])

for i in range(n):
    for j in range(i):
        if li[i] > li[j]:
            if dp[j] + 1 > dp[i]:
                graph[i].clear()
                dp[i] = dp[j] + 1
                for k in graph[j]:
                    graph[i].append(k)
                graph[i].append(li[i])
    if len(graph[i]) == 0:
        graph[i].append(li[i])

# print(graph)
# print(dp)
graph.sort(key=lambda x: -len(x))
print(len(graph[0]))
for x in graph[0]:
    print(x, end=' ')
# 6
# 1 4 2 3 5 4

# 7
# 2 1 4 2 3 5 4