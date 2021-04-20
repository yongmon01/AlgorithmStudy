from collections import deque
def bfs(graph, start, visited):
    return_list = []
    q = []
    q.append(start)
    for i in range(len(graph)):
        graph[i] = deque(graph[i])
    while q:
        node = q.pop()
        return_list.append(node)
        if len(graph[node]) != 0:
            next_node = graph[node].popleft()
            q.append(next_node)
    return return_list

def solution(tickets):
    airports_num = dict()
    airports = set()
    for i in tickets:
        airports.add(i[0])
        airports.add(i[1])
    airports = list(airports)
    airports.sort()
    print(airports)
    for i in range(1,len(airports)+1):
        airports_num[airports[i-1]] = i
    print(airports_num)

    graph = [[] for _ in range(len(airports)+1)]

    for i in tickets:
        a, b = airports_num[i[0]], airports_num[i[1]]
        graph[a].append(b)
    # for i in range(len(graph)):
    #     graph[i].sort()

    print('graph?',graph)

    visited = [False] * (len(airports)+1)
    li = bfs(graph, airports_num["ICN"], visited)
    print(li)
    answer = []
    for i in li:
        answer.append(airports[i-1])
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))



