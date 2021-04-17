# n = int(input())
# t=[0]*n;p=[0]*n
# for i in range(n):
#     t[i],p[i]=map(int,input().split())
# d = [0]*(n+1)
# for i in range(n+1):
#     print(d)
#     for j in range(i):
#         if j+t[j] <= i and d[j] + p[j] >= d[i]:
#             d[i] = d[j] + p[j]
# print(d[n])

n = int(input())
time = []
point = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    point.append(p)
#
# print(time)
# print(point)

dp = [0] * (n+1)
for i in range(n+1):
    if i == n:
        continue
    t = time[i]
    p = point[i]
    if dp[i] == 0 and i != 0:
        dp[i] = max(dp[:i])
    if i + t <= n:
        dp[i+t] = max(dp[i+t], dp[i] + p)

print(dp)


# n = int(input())
# time = []
# point = []
# for i in range(n):
#     t, p = map(int, input().split())
#     time.append(t)
#     point.append(p)
#
# print(time)
# print(point)
#
# def gogo(start, end, earn):
#     # print(start, end, earn)
#     if start > end:
#         return earn
#     take = gogo(start + time[start], end, earn + point[start])
#     skip = gogo(start + 1, end, earn)
#     if start + time[start] -1 > end:
#         return skip
#     return max(take, skip)
#
# print(gogo(0, n-1, 0))

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
