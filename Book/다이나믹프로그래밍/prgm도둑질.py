def m(money):
    dp = [0] * (len(money))
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, len(money)):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    return dp[-1]

def solution(money):
    if len(money) == 3:
        return max(money)
    elif len(money) == 4:
        return max(money[0]+money[2], money[1]+money[3])

    # 1번째 선택
    m1 = m(money[2:len(money)-1]) + money[0]
    # 마지막 선택
    m2 = m(money[1:len(money)-2]) + money[-1]
    # 둘다 선택안함
    m3 = m(money[1:len(money)-1])
    return max(m1,m2,m3)

money = [1,2,3]
print(solution(money))


# 답은 맞는듯하나 시간초과 ㅠㅠ
# def solution(money):
#     # 첫번째 선택
#     answer1 = choice(money, 2, len(money)-1, money[0])
#     # 마지막 선택
#     answer2 = choice(money,1,len(money)-2,money[-1])
#     # 첫번째 마지막 둘다 선택 안함
#     answer3 = choice(money, 1, len(money)-1, 0)
#     return max(answer1, answer2, answer3)
#
# def choice(money, i, n, max_money):
#     if i >= n:
#         return max_money
#     return max(choice(money, i+2, n, max_money+money[i]), choice(money, i+1, n, max_money))
#
# money = [1,2,3,1]
# print(solution(money))