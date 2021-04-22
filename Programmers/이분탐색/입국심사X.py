def solution(n, times):
    right = min(times) * n
    left = 1
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        temp = n
        for i in times:
            temp -= mid//i
            if temp <= 0:
                answer = mid
                right = mid - 1
                break
        if temp > 0:
            left = mid + 1
    return answer

n = 6
times = [7, 10]
print(solution(n, times))