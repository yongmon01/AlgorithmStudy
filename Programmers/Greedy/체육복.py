# 역시 쉬운 문제라도 문제의 조건, 인과관계를 잘 파악하자.
def solution(n, lost, reserve):
    answer = 0
    state = [1] * (n + 1)
    state[0] = 0
    for i in reserve:
        state[i] += 1
    for i in lost:
        state[i] -= 1

    for i in range(1, len(state)):
        if state[i] == 0 and state[i - 1] == 2:
            state[i - 1] = 1
            state[i] = 1
        elif state[i] == 0 and i < len(state) - 1 and state[i + 1] == 2:  #
            state[i + 1] = 1
            state[i] = 1

    return state.count(1) + state.count(2)