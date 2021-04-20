def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    print(routes)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top in routes and routes[top]:
            stack.append(routes[top].pop())
        else:
            path.append(stack.pop())
    return path[::-1]

tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]
print(solution(tickets))