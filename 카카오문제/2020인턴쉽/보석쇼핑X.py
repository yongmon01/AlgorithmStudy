# 97.8 ...

def solution(gems):
    answer = []
    gems_set = set(gems)
    gems_set = list(gems_set)
    print(gems_set)

    i, j = 0, 0
    while i < len(gems):
        dic = dict()
        for k in gems_set:
            dic[k] = 0
        count = 0
        while i < len(gems) and count < len(gems_set):
            if dic[gems[i]] == 0:
                count += 1
            dic[gems[i]] += 1
            i += 1

        # if i >= len(gems) and j != 0:
        #     break

        while j < len(gems) and count >= len(gems_set):

            if dic[gems[j]] >= 1:
                dic[gems[j]] -= 1
            if dic[gems[j]] == 0:
                count -= 1
            if count < len(gems_set):
                break
            j += 1

        # if not answer:
        #     answer.append((j, i - 1))
        # elif answer[-1][0] == j:
        #     continue
        # else:
        #     answer.append((j, i-1))
        answer.append((j, i - 1))

        if i < len(gems)-1:
            j += 1
            i = j

    print(answer)
    answer.sort(key = lambda x: abs(x[0]-x[1]))
    return [answer[0][0]+1, answer[0][1]+1]


print(solution(["XYZ", "XYZ", "XYZ"]))