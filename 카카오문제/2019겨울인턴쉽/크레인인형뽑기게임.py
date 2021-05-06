# 무난히 완큐에 해결!

def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if stack and stack[-1] == board[i][m-1]:
                    answer += 2
                    del stack[-1]
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))