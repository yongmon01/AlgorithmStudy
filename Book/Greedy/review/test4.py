def count(n, num, dp):
    if dp[n] != -1:
        return dp[n]

    if n % num != 0:
        return 0
    else:
        dp[n] = count(n // num, num, dp) + 1
    return dp[n]

def solution(n):
    answer = 0
    dp = [-1] * (n+1)

    for i in range(1, n+1):
        answer += count(i, 5, dp)

    return answer

print(solution(100000))


# def solution(n):
#     answer = 0
#     dp = [-1] * (n+1)
#
#     def count(n, num):
#         if dp[n] != -1:
#             return dp[n]
#
#         if n % num != 0:
#             return 0
#         else:
#             dp[n] = count(n // num, num) + 1
#         return dp[n]
#
#     for i in range(1, n+1):
#         answer += count(i, 5)
#
#     return answer