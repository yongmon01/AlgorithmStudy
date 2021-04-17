# bisect_left 를 썼음에도 시간 초과. 아마 del scoville[0] 연산이 계속 되어서 같다.
# from bisect import bisect_left
#
# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while scoville[0] < K:
#         if len(scoville) == 1:
#             return -1
#         new_num = scoville[0] + scoville[1] * 2
#         del scoville[0]
#         del scoville[0]
#         index = bisect_left(scoville, new_num)
#         scoville.insert(index, new_num)
#         answer += 1
#     return answer
#
# print(solution([1, 2, 3, 9, 10, 12], 7))

# 우선순위큐로 통과
import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    while True:
        first = heapq.heappop(q)
        if first >= K:
            return answer
        if len(q) == 0:
            return -1
        second = heapq.heappop(q)
        heapq.heappush(q, first + 2 * second)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))