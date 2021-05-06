# 패배인정.. 이풀이는 같은칸에 위에서오는경우 왼쪽에서오는경우 같은때를 고려못함.

from collections import deque

def bfs(x,y,board):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    cost = [[int(1e9)] * len(board[0]) for _ in range(len(board))]
    cost[0][0] = 0
    prev_coordi = [[-1] * len(board[0]) for _ in range(len(board))]
    prev_coordi[0][0] = [0,0]
    prev_coordi[0][1] = [0,0]
    prev_coordi[1][0] = [0,0]
    print("cost", cost)
    print("prev_coordi", prev_coordi)

    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        tmp = cost[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                if board[nx][ny] == 0:
                    c1 = 100
                    c2 = 0
                    prev_x = prev_coordi[x][y][0]
                    prev_y = prev_coordi[x][y][1]
                    if nx != prev_x and ny != prev_y:
                        c2 = 500
                    tmp_cost = c1 + c2 + tmp
                    if tmp_cost < cost[nx][ny]:
                        cost[nx][ny] = tmp_cost
                        # print('nx, ny ',nx,ny)
                        # print('x, y ',x,y)
                        prev_coordi[nx][ny] = [x, y]
                        q.append((nx, ny))

    print(prev_coordi)
    print(cost)


def solution(board):
    answer = 0
    bfs(0,0,board)
    return answer

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))