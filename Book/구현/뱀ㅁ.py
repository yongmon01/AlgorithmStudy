n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]
# 사과 배치
for i in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
# x초때 방향
L = int(input())
d_change = []
for i in range(L):
    a, b = input().split()
    d_change.append((int(a), b))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
now_d = 0

snake = [(0, 0)]
count = 0
print(graph)
while True:
    if len(d_change) != 0:
        if d_change[0][0] == count:
            if d_change[0][1] == 'L':
                now_d -= 1
            else:
                now_d += 1
            del d_change[0]
        if now_d == -1:
            now_d = 3
        if now_d == 4:
            now_d = 0

    # 사과 쳐먹음 ################## 머리만 단다
    if graph[snake[0][0]][snake[0][1]] == 1:

        graph[snake[0][0]][snake[0][1]] = 0

        x = snake[0][0] + dx[now_d]
        y = snake[0][1] + dy[now_d]
        snake.insert(0, (x, y))
    # 사과 안쳐먹음
    else:
        x = snake[0][0] + dx[now_d]
        y = snake[0][1] + dy[now_d]
        snake.insert(0, (x, y))
        if snake[0] in snake[1:]:
            print("벽에부딪힌건아님")
            break
        del snake[-1]
    print(snake)
    if x < 0 or y < 0 or x >= n or y >= n:
        break
    if snake[0] in snake[1:]:
        print("벽에부딪힌건아님")
        break
    prev_tail = snake[-1]
    count += 1
print(count+1)





# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L


# n = int(input())
# k = int(input())
# graph = [[0]*(n) for _ in range(n)]
# for i in range(k):
#     x, y = map(int, input().split())
#     graph[x-1][y-1] = 1
# L = int(input())
# d_change = []
# for i in range(L):
#     a, b = input().split()
#     d_change.append((int(a), b))
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# now_d = 0
# prev_d = 0
# apple_ate = False
# prev_tail = None
#
# snake = [(0, 0)]
# count = 0
# print(graph)
# while True:
#     if len(d_change) != 0:
#         if d_change[0][0] == count:
#             if d_change[0][1] == 'L':
#                 now_d -= 1
#             else:
#                 now_d += 1
#             del d_change[0]
#         if now_d == -1:
#             now_d = 3
#         if now_d == 4:
#             now_d = 0
#     # 사과 쳐먹음
#     if graph[snake[0][0]][snake[0][1]] == 1:
#         # x = snake[0][0] + dx[now_d]
#         # y = snake[0][1] + dy[now_d]
#         # snake.insert(0, (x, y))
#         graph[snake[0][0]][snake[0][1]] = 0
#         snake.append(prev_tail)
#         x = snake[0][0] + dx[now_d]
#         y = snake[0][1] + dy[now_d]
#         for i in range(len(snake) - 1):
#             snake[len(snake) - 1 - i] = snake[len(snake) - 2 - i]
#         del snake[0]
#         snake.insert(0, (x, y))
#     # 사과 안쳐먹음
#     else:
#         x = snake[0][0] + dx[now_d]
#         y = snake[0][1] + dy[now_d]
#         for i in range(len(snake)-1):
#             snake[len(snake)-1-i] = snake[len(snake)-2-i]
#         del snake[0]
#         snake.insert(0, (x, y))
#     print(snake)
#     if x < 0 or y < 0 or x >= n or y >= n:
#         break
#     if snake[0] in snake[1:]:
#         print("벽에부딪힌건아님")
#         break
#     prev_tail = snake[-1]
#     count += 1
# print(count+1)
#
#
#
#
#
# # 6
# # 3
# # 3 4
# # 2 5
# # 5 3
# # 3
# # 3 D
# # 15 L
# # 17 D
#
# # 10
# # 4
# # 1 2
# # 1 3
# # 1 4
# # 1 5
# # 4
# # 8 D
# # 10 D
# # 11 D
# # 13 L
#
# # 10
# # 5
# # 1 5
# # 1 3
# # 1 2
# # 1 6
# # 1 7
# # 4
# # 8 D
# # 10 D
# # 11 D
# # 13 L