from collections import deque
# 3(hi)
# 3(hi)v
# 2(2(hi)v)
# 2(2(hi)v3(abc))
# 10(p)
# 11(pc)
string = "q2(2(k)o2(j)v)" # 틀림..

chars = []
parentheses = deque()
counts = deque()
strings = deque()

num, word = "", ""
for i in range(len(string)):
    if string[i] == '(' or string[i] == ')':
        chars.append(string[i])
    elif string[i] >= '0' and string[i] <= '9':
        num += string[i]
        if string[i+1] < '0' or string[i+1] > '9':
            chars.append(num)
            num = ""
    elif string[i] >= 'a' and string[i] <= 'z':
        word += string[i]
        if i == len(string)-1:
            chars.append(word)
            word = ""
        elif string[i+1] < 'a' or string[i+1] > 'z':
            chars.append(word)
            word = ""
print(chars)

answer = ""
for i in range(len(chars)):
    if chars[i] == '(':
        parentheses.append(chars[i])
    elif chars[i] == ')':
        parentheses.pop()
        c = counts.pop()
        try:
            s = strings.pop()
            answer += int(c) * s
        except:
            answer = int(c) * answer
    elif chars[i].isdigit():
        counts.append(chars[i])
    elif chars[i].isalpha():
        if i == 0:
            answer += chars[i]
        elif chars[i-1] == ')':
            answer += chars[i]
        else:
            strings.append(chars[i])

print(answer)

