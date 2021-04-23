# 무난히 풀었다. any 함수도 새로 배웠다.

from collections import deque

def solution(priorities, location):
    n = priorities[location]
    turn = []
    for i in range(len(priorities)):
        priorities[i] = (priorities[i], i)
    print(priorities)
    q = deque(priorities)
    while q:
        p, index = q.popleft()
        # if not q:
        #     turn.append((p, index))
        # elif p < max([i[0] for i in list(q)]):
        #     q.append((p, index))
        if any(p < i[0] for i in q):
            q.append((p, index))
        else:
            turn.append((p, index))
    print(turn)

    return turn.index((n, location)) + 1


# def solution(priorities, location):
#     n = priorities[location]
#     turn = []
#     for i in range(len(priorities)):
#         priorities[i] = (priorities[i], i)
#     print(priorities)
#     q = deque(priorities)
#     while q:
#         p, index = q.popleft()
#         print([i[0] for i in list(q)])
#         if not q:
#             turn.append((p, index))
#         elif p < max([i[0] for i in list(q)]):
#             q.append((p, index))
#         else:
#             turn.append((p, index))
#     print(turn)
#
#     return turn.index((n, location)) + 1

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))