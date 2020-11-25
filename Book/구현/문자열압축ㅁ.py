input_string = input()
n = len(input_string)
min_length = n

for i in range(1, n//2 + 1):
    word_list = []
    for j in range(0, n-n % i, i):
        word_list.append(input_string[j:j+i])
    word_list.append(input_string[n-n % i:])
    word_list.append(None)
    prev = None
    count = 1
    return_string = ""
    for j in word_list:
        current = j
        if j == prev:
            count += 1
        elif j != prev and prev is not None:
            return_string += str(count) + prev if count != 1 else prev
            count = 1
        prev = current
    print(return_string)
    min_length = min(min_length, len(return_string))

print(min_length)


# def solution(s):
#     answer = len(s)
#     for i in range(1, len(s)//2+1):
#         prev = s[0:i]
#         count = 1
#         return_str = ""
#         for j in range(i, len(s), i):
#             current_str = s[j:j+i]
#             if current_str == prev:
#                 count += 1
#             else:
#                 return_str += str(count) + prev if count >= 2 else prev
#                 prev = current_str
#                 count = 1
#         return_str += str(count) + prev if count >= 2 else prev
#         answer = min(answer, len(return_str))
#     return answer
#
# solution('abababz')
