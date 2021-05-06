# 좀더 나은 방식..

def solution(s):
    li = []
    i = 0
    dictionary = dict()
    while i < len(s):
        if s[i].isdigit():
            char, index = extract(s, i)
            li.append(char)
            i = index + 1
        else:
            i += 1

    li = [int(i) for i in li]
    for i in li:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 0

    # 딕셔너리의 .items() 사용
    answer = sorted(dictionary.items(), key=lambda x:-x[1])
    return [i[0] for i in answer]

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

# 사실 이방법이 숫자들을 리스트에 담는데 더 쉽다.
# s = "{{20,111},{111}}"
# s = s[2:-2]
# li = s.split('},{')
# nums = []
#
# for i in li:
#     k = i.split(',')
#     for n in k:
#         nums.append(n)
#
# print(nums)