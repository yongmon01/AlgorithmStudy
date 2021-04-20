def solution(p):
    if isCorrect(p) is True:
        return p
    u, v = u_v(p)
    if isCorrect(u) is True:
        return u + solution(v)
    else:
        new_s = '('
        new_s += solution(v)
        new_s += ')'
        new_s += delete_and_reverse(u)
        return new_s


def u_v(string):
    count = 0
    for i in range(len(string)):
        if string[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return string[:i + 1], string[i + 1:]


def isCorrect(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True


def delete_and_reverse(string):
    string = string[1:len(string) - 1]
    return_string = ''
    for i in string:
        if i == '(':
            return_string += ')'
        else:
            return_string += '('
    return return_string