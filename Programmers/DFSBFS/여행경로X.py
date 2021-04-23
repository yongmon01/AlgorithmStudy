# 쉽게 생각하다가 틀렸다.. 기존의 bfs문제와 다르다. 사이클이 발생하는 경우 까지 생각하고 올바르게 처리해야함.
# 아래는 틀린풀이. 사이클이 발생하는 경우를 생각못하고 visited 변수를 사용했다.
from collections import deque
def bfs(graph, start, visited):
    return_list = []
    q = deque()
    q.append(start)
    while q:
        station = q.popleft()
        return_list.append(station)
        for i in graph[station]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)
    return return_list

def solution(tickets):
    airports_num = dict()
    airports = set()
    for i in tickets:
        airports.add(i[0])
        airports.add(i[1])
    airports = list(airports)
    print(airports)
    for i in range(1,len(airports)+1):
        airports_num[airports[i-1]] = i
    print(airports_num)

    graph = [[] for _ in range(len(airports)+1)]

    for i in tickets:
        a, b = airports_num[i[0]], airports_num[i[1]]
        graph[a].append(b)
    for i in range(len(graph)):
        graph[i].sort()

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



