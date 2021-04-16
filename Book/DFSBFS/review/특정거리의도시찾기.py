# 아 맞았다... 난 틀리지않았어..
# input = sys.stdin.readline 안 넣으면 무조건 시간초과
import sys
input = sys.stdin.readline
# 도시개수, 도로개수, 거리, 출발
n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited[x] = True

print('graph',graph)
print('visited',visited)
# print('answer',answer)
answer = [x]
for i in range(k):
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

# 다익스트라 풀이
# import sys
# from collections import deque
# input = sys.stdin.readline
# n, m, k, x = map(int, input().split())
# # 도시 도로 거리 출발
#
# graph = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#
# # print(graph)
# distance = [int(1e9)] * (n+1)
# distance[x] = 0
#
# q = deque()
# q.append((0, x))
# while q:
#     d1, n1 = q.popleft()
#     if d1 < distance[n1]:
#         continue
#     for i in graph[n1]:
#         if d1 + 1 < distance[i]:
#             distance[i] = d1 + 1
#             q.append((distance[i], i))
#
# if k not in distance:
#     print(-1)
# else:
#     for i in range(n+1):
#         if distance[i] == k:
#             print(i)