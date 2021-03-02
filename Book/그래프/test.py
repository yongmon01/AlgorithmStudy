n = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
graph = [[False] * (n + 1) for i in range(n + 1)]

# 작년 순위 정보 입력
data = list(map(int, input().split()))
# 방향 그래프의 간선 정보 초기화
for i in range(n):
    for j in range(i + 1, n):
        graph[data[i]][data[j]] = True
        indegree[data[j]] += 1

print(graph)
print(indegree)