n = int(input())
move = input().split()
a, b = 1, 1

for i in move:
    if i == 'U' and a >= 2:
        a -= 1
    elif i == 'D' and a <= n-1:
        a += 1
    elif i == 'R' and b <= n-1:
        b += 1
    elif i == 'L' and b >= 2:
        b -= 1

print(a, b)

# n = int(input())
# plans = input().split()
# x, y = 1, 1
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in plans:
#     for i in range(4):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or nx > n or ny < 1 or ny > n:
#         continue
#     x = nx
#     y = ny
#
# print(x, y)


