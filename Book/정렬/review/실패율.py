# 계수정렬을 이용한 내 멋진 풀이. 시간복잡도 최강.

def solution(N, stages):
    answer = []
    csort = [0] * (N + 2)
    for i in stages:
        csort[i] += 1
    total = sum(csort)
    left = 0
    for i in range(1, len(csort) - 1):  #
        left = csort[i]
        if total == 0:
            answer.append((0, i))
        else:
            answer.append((left / total, i))
        total -= csort[i]
    answer.sort(key=lambda x: (-x[0], x[1]))

    return [i[1] for i in answer]