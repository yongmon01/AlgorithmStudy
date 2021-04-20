# 풀었다.. 교재의 "퇴사" 문제와 비교해볼것
import copy
def solution(money):
    n = len(money)
    dp1 = copy.deepcopy(money[:n-1]) # 첫번째 선택
    dp2 = copy.deepcopy(money[1:n+1]) # 첫번째 선택x
    dp1[2] += dp1[0]
    dp2[2] += dp2[0]
    for i in range(3, n-1):
        dp1[i] = max(dp1[i-2], dp1[i-3]) + money[i]
        dp2[i] = max(dp2[i-2], dp2[i-3]) + money[i+1]

    return max(max(dp1), max(dp2))

money = [1, 100, 2, 3, 100]
print(solution(money))


# 답은 맞지만 시간초과.
# import copy
# def solution(money):
#     n = len(money)
#     dp1 = copy.deepcopy(money[:n-1]) # 첫번째 선택
#     dp2 = copy.deepcopy(money[1:n+1]) # 첫번째 선택x
#     for i in range(n-1):
#         for j in range(i-1):
#             if dp1[i] < dp1[j] + money[i]:
#                 dp1[i] = dp1[j] + money[i]
#             if dp2[i] < dp2[j] + money[i+1]:
#                 dp2[i] = dp2[j] + money[i+1]
#
#     return max(max(dp1), max(dp2))



# def m(money):
#     dp = [0] * (len(money))
#     dp[0] = money[0]
#     dp[1] = max(money[0], money[1])
#     for i in range(2, len(money)):
#         dp[i] = max(dp[i-2] + money[i], dp[i-1])
#     return dp[-1]
#
# def solution(money):
#     if len(money) == 3:
#         return max(money)
#     elif len(money) == 4:
#         return max(money[0]+money[2], money[1]+money[3])
#
#     # 1번째 선택
#     m1 = m(money[2:len(money)-1]) + money[0]
#     # 마지막 선택
#     m2 = m(money[1:len(money)-2]) + money[-1]
#     # 둘다 선택안함
#     m3 = m(money[1:len(money)-1])
#     return max(m1,m2,m3)