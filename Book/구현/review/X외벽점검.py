from collections import deque
from itertools import permutations
def solution(n, weak, dist):
    answer = []
    m = len(weak)
    weak = weak + [i + n for i in weak]
    print(weak)

    for r in range(m+1):
        can = list(permutations(dist, len(dist)))
        print(can)
        for i in can:
            q = deque(weak[r: r + m])
            print(q)
            # print(q)
            j = 0
            count = 0
            while q:
                node = q.popleft()
                count += 1
                # 친구들을 다투입해도 해결 못하는 경우
                if j >= len(dist):
                    count = int(1e9)
                    break
                node_plus_dist = node + i[j]
                while q and node_plus_dist >= q[0]:
                    q.popleft()
                j += 1
            answer.append(count)
    print(answer)

    if min(answer) == int(1e9):
        return -1
    else:
        return min(answer)

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3]
solution(n, weak, dist)