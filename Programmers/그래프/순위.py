# 교재 최단경로파트의 '정확한 순위' 문제와 동일.
def solution(n, results):
    answer = 0

    graph = [[int(1e9)] * (n + 1) for _ in range(n + 1)]
    for i in results:
        graph[i[1]][i[0]] = 1
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                graph[i][j] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for k in range(1, n + 1):
        count = 0
        for i in range(1, n + 1):
            if graph[k][i] != int(1e9):
                count += 1
        for j in range(1, n + 1):
            if graph[j][k] != int(1e9):
                count += 1
        if graph[k][k] != int(1e9):
            count -= 1
        if count == n:
            answer += 1

    return answer
