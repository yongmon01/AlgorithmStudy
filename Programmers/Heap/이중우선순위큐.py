import heapq

def solution(operations):
    count = 0

    q = []

    for i in operations:
        if i.startswith("I"):
            num = int(i[2:])
            heapq.heappush(q, num)
            count += 1
        elif i == "D -1" and count >= 1:
            heapq.heappop(q)
            count -= 1
        elif i == "D 1" and count >= 1:
            max_num = max(q)
            q.remove(max_num)
            count -= 1
    if count == 0:
        return [0,0]
    max_num = max(q)
    return (max_num, heapq.heappop(q))

operations = ["I 2", "I 3", "D -1", "D 1", "I 4"]
print(solution(operations))

# import heapq
#
# def solution(operations):
#     count = 0
#
#     positive_q = []
#     negative_q = []
#
#     for i in operations:
#         if i.startswith("I"):
#             num = int(i[2:])
#             heapq.heappush(positive_q, num)
#             heapq.heappush(negative_q, -num)
#             count += 1
#         elif i == "D -1" and count >= 1:
#             heapq.heappop(positive_q)
#             count -= 1
#         elif i == "D 1" and count >= 1:
#             heapq.heappop(negative_q)
#             count -= 1
#
#     if count > 0:
#         return [-heapq.heappop(negative_q), heapq.heappop(positive_q)]
#     else:
#         return [0, 0]
#
#     # # 최소 뽑기
#     # print(heapq.heappop(positive_q))
#     # # 최대 뽑기
#     # print(heapq.heappop(negative_q))
#
# operations = ["I 2", "I 3", "D -1", "D 1", "I 4"]
# print(solution(operations))


# import heapq
#
# q = []
# heapq.heappush(q,2)
# heapq.heappush(q,3)
# heapq.heappush(q,1)
# heapq.heappush(q,5)
# heapq.heappush(q,4)
# q.sort(reverse=True)
# print(q)
# print(heapq.heappop(q))