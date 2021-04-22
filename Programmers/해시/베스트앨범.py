genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    dictionary = dict()
    for i in range(len(genres)):
        if genres[i] not in dictionary:
            dictionary[genres[i]] = [plays[i], (plays[i], i)]
        else:
            dictionary[genres[i]].append((plays[i],i))
            dictionary[genres[i]][0] += plays[i]

    li = list(dictionary.values())
    for i in range(len(li)):
        total = li[i][0]
        del li[i][0]
        li[i].sort(key=lambda x: (-x[0], x[1]))
        li[i].insert(0, total)
    li.sort(key=lambda x:(-x[0]))

    for i in li:
        if len(i) >= 3:
            answer.append(i[1][1])
            answer.append(i[2][1])
        else:
            answer.append(i[1][1])
    return answer

print(solution(genres, plays))