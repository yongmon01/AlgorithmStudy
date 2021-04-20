# https://dalpaeng00.tistory.com/42?category=897781 참고해서 품..

def solution(name):
    answer, n = 0, len(name)
    name_char = list(name)
    i = 0
    while True:
        print(name_char)
        if name_char[i] <= 'N':
            cc = ord(name_char[i]) - ord('A')
        elif name_char[i] > 'N':
            cc = ord('Z') - ord(name_char[i]) + 1
        answer += cc
        name_char[i] = 'A'

        if name_char == ['A'] * n:
            break

        left, right = 1, 1
        while i + right < n and name_char[i + right] == 'A':
            right += 1
        while i - left >= -n and name_char[i - left] == 'A':
            left += 1

        if right > left:
            i -= left
            answer += left
        else:
            i += right
            answer += right

    return answer

print(solution("JEROEN"))


# 틀림.. ABAAAAB 같은경우는 우좌좌 면 끝나는 반례..
# def solution(name):
#     answer = 0
#     for i in name:
#         if i <= 'N':
#             cc = ord(i) - ord('A')
#         elif i > 'N':
#             cc = ord('Z') - ord(i) + 1
#         answer += cc
#         print(cc)
#     print(left_right(name[1:]))
#     return answer + left_right(name[1:])
#
# def left_right(name):
#     left, right = 0, 0
#     while left < len(name) and name[left] == 'A':
#         left += 1
#     while right < len(name) and name[len(name)-1-right] == 'A':
#         right += 1
#     # print(left, right)
#     # print(ord('A'))
#     return len(name) - max(left, right)
#
