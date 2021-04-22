# dp 같은 방식으로 풀었는데 실패..
from collections import deque
def solution(people, limit):
    answer = 0
    index = [i for i in range(limit+1)]
    print(index)
    dp = [0] * (limit + 1)
    for i in people:
        dp[i] += 1
    print(dp)

    for i in range(1, limit // 2):
        j = limit
        while dp[i] != 0 and i < j:
            if i + j > limit: # =?
                j -= 1
                continue
            else:
                if dp[i] >= dp[j]:
                    dp[i] -= dp[j]
                    answer += dp[j]
                    dp[j] = 0
                else:
                    dp[j] -= dp[i]
                    answer += dp[i]
                    dp[i] = 0
                j -= 1

    for i in range(limit//2, limit + 1):
        if i * 2 <= limit and dp[i] != 0:
            answer += (dp[i]//2 + dp[i] % 2)
        else:
            answer += dp[i]
    return answer

people = [1,1,5,5,9]
limit = 10
# people = [2,3,3,4,5,5,7,8]
# limit = 10
# people = [70, 50, 80, 50]
# limit = 100
print(solution(people,limit))



# from collections import deque
# def solution(people, limit):
#     answer = 0
#     index = [i for i in range(limit+1)]
#     print(index)
#     dp = [0] * (limit + 1)
#     for i in people:
#         dp[i] += 1
#     print(dp)
#
#     for i in range(1, limit // 2):
#         j = limit
#         while dp[i] != 0 and i <= j:
#             if i + j > limit: # =?
#                 j -= 1
#                 continue
#             else:
#                 if dp[i] >= dp[j]:
#                     dp[i] -= dp[j]
#                     answer += dp[j]
#                     dp[j] = 0
#                 else:
#                     dp[j] -= dp[i]
#                     answer += dp[i]
#                     dp[i] = 0
#                 j -= 1
#
#     for i in range(limit//2, limit + 1):
#         if i * 2 <= limit and dp[i] != 0:
#             answer += (dp[i]//2 + dp[i] % 2)
#         else:
#             answer += dp[i]
#     return answer
#
# people = [2,3,3,4,5,5,7,8]
# limit = 10
# # people = [70, 50, 80, 50]
# # limit = 100
# print(solution(people,limit))





# from collections import deque
# def solution(people, limit):
#     answer = 0
#     index = [i for i in range(limit+1)]
#     print(index)
#     dp = [0] * (limit + 1)
#     for i in people:
#         dp[i] += 1
#     print(dp)
#
#     for i in range(1, limit+1):
#         j = limit
#         while dp[i] != 0 and i <= j:
#             if i + j > limit: # =?
#                 j -= 1
#                 continue
#             else:
#                 if dp[i] >= dp[j]:
#                     dp[i] -= dp[j]
#                     answer += dp[j]
#                     dp[j] = 0
#                 else:
#                     dp[j] -= dp[i]
#                     answer += dp[i]
#                     dp[i] = 0
#                 j -= 1
#
#     return answer
#
# # people = [2,3,3,4,5,5,7,8]
# # limit = 10
# people = [70, 50, 80, 50]
# limit = 100
# print(solution(people,limit))