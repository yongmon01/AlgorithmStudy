# 내풀이.. 멋진걸.
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

# 다른사람풀이
# def solution(n, times):
#     right = min(times) * n
#     left = 1
#     answer = 0
#     while left <= right:
#         mid = (right + left) // 2
#         temp = n
#         for i in times:
#             temp -= mid//i
#             if temp <= 0:
#                 answer = mid
#                 right = mid - 1
#                 break
#         if temp > 0:
#             left = mid + 1
#     return answer