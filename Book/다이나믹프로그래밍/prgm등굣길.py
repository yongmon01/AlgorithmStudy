def solution(m, n, puddles):
    graph = [[0]*(m) for _ in range(n)]
    print(graph)

    for i in puddles:
        graph[i[1]-1][i[0]-1] = -1
    print(graph)

    for i in range(1, m):
        if graph[0][i-1] != -1 and graph[0][i] != -1:
            graph[0][i] = 1
        else:
            graph[0][i] = -1
    for i in range(1, n):
        if graph[i][0] != -1 and graph[i-1][0] != -1:
            graph[i][0] = 1
        else:
            graph[i][0] = -1

    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] == -1:
                continue
            elif graph[i-1][j] == -1 and graph[i][j-1] == -1:
                graph[i][j] = -1
            elif graph[i-1][j] == -1:
                graph[i][j] = graph[i][j - 1]
            elif graph[i][j-1] == -1:
                graph[i][j] = graph[i-1][j]
            else:
                graph[i][j] = graph[i][j - 1] + graph[i-1][j]
    print(graph)
    return graph[n-1][m-1] % 1000000007

print(solution(4,3,[[2,2],[1,2]]))