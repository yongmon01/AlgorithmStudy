# def knapsack(k, w, v, n):
#     if k <= 0 or n <= 0:
#         return 0
#     if w[n-1] > k:
#         return knapsack(k, w, v, n-1)
#     carry = v[n - 1] + knapsack(k - w[n-1], w, v, n-1)
#     leave = knapsack(k, w, v, n-1)
#     return max(carry, leave)
#
# print(knapsack(50,[10,20,30],[60,100,120],3))



n, k = map(int,input().split())
w = []
v = []
for i in range(n):
    x, y = map(int, input().split())
    w.append(x)
    v.append(y)

def hum(i, weight):
    if weight > k:
        return 0
    if i >= n:
        return 0
    choose = 0
    if weight+w[i] <= k:
        choose = v[i] + hum(i+1, weight+w[i])
    no_choose = hum(i+1, weight)
    return max(choose, no_choose)

print(hum(0, 0))
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

















