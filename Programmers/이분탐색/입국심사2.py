def solution(n, times):

    l, r = 0, min(times) * n
    answer = r
    while l <= r:
        mid = (l + r) // 2
        # print('l r mid ',l, r, mid)
        now = n
        for i in times:
            now -= (mid // i)
        # print(now)
        if now <= 0:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
    return answer

n = 6
times = [7, 10]
print(solution(n, times))