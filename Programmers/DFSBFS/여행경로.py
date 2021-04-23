from collections import deque

def solution(tickets):
    dictionary, answer = dict(), []
    for f, d in tickets:
        if f in dictionary:
            dictionary[f].append(d)
        else:
            dictionary[f] = [d]

    for i in dictionary:
        dictionary[i].sort(reverse=True)

    q = deque()
    q.append("ICN")
    while q:
        node = q[-1]
        if node not in dictionary or not dictionary[node]:
            answer.append(q.pop())
        else:
            q.append(dictionary[node][-1])
            del dictionary[node][-1]

    return answer[::-1]

    # print(dictionary)

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))