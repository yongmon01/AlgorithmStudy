# 위상정렬 풀이

from collections import deque

n = int(input())
come = [[] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
times = [0] * (n+1)
answers = [0] * (n+1)
for i in range(1, n+1):
    li = list(map(int, input().split()))
    times[i] = li[0]
    for j in li[1:]:
        if j != -1:
            graph[j].append(i)
            come[i].append(j)
# print(come)
# print(graph)

q = deque()
for i in range(1, n+1):
    if len(come[i]) == 0:
        q.append(i)
        answers[i] = times[i]

while q:
    node = q.popleft()
    # print('pop node: ', node)
    t = answers[node]
    for i in graph[node]:
        # print('i ',i)
        # print('answers[i] ',answers[i],' t ',t,' times[i] ',times[i])
        answers[i] = max(answers[i], t + times[i])
        come[i].remove(node)
        if len(come[i]) == 0:
            q.append(i)

print(times)
print(answers)



# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# dp 풀이 (입력이 1번노드, 2번노드, 3번노드 ... 순으로 입력되니 가능한거 같다)
# n = int(input())
# come = [[] for _ in range(n+1)]
# times = [0] * (n+1)
# for i in range(1,n+1):
#     li = list(map(int, input().split()))
#     time = li[0]
#     prev_time = 0
#     del li[0]
#     for j in li:
#         if j != -1:
#             prev_time = max(prev_time, times[j])
#     times[i] = prev_time + time
# print(times)