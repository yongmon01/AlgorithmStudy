import heapq


def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    prev = 0

    n = len(q)
    total = 0
    while q and total + (q[0][0] - prev) * n <= k:
        t, index = heapq.heappop(q)
        total += (t - prev) * n
        n -= 1
        prev = t

    q.sort(key=lambda x: x[1])
    # 더 먹을게 없는 경우
    if len(q) == 0:
        return -1
    return q[(k - total) % len(q)][1]

print(solution([3,1,2],5))