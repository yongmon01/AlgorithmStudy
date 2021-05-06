# 정답은 맞지만 굳이 이렇게 풀필요가 없었다.
# 그래도 시험때는 이렇게라도 맞자.

def solution(s):

    s = s[2:-2]
    answer = s.split('},{')
    answer.sort(key = lambda x: len(x))
    print(answer)
    li = [[] for _ in range(len(answer))]

    for i in range(len(answer)):
        tmp = answer[i]
        k = 0

        while k < len(tmp):
            if tmp[k].isdigit():
                string, index = extract(tmp, k)
                li[i].append(string)
                k = index + 1
            else:
                k += 1
    print('li ',li)
    return_answer = []

    for i in li:
        for j in i:
            if j not in return_answer:
                return_answer.append(j)

    return [int(i) for i in return_answer]

def extract(string, j):
    answer, index = "", 0
    for i in range(j, len(string)):
        index = i
        answer += string[i]
        if i + 1 < len(string):
            if string[i+1].isdigit():
                continue
            else:
                break
    return answer, index

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
