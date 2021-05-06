# 수식최대화2를 참고한 내풀이.

from itertools import permutations
import re

def solution(expression):
    answer = []
    # oper = set()
    # for i in expression:
    #     if not i.isdigit():
    #         oper.add(i)
    # oper = list(oper)
    oper = [x for x in ['*', '+', '-'] if x in expression] # 위 5줄을 한줄로 만들수있는 코드

    opers = list(list(x) for x in permutations(oper, len(oper)))
    li = re.split(r'(\D)', expression) # 정규표현식

    print('opers',opers)
    print('li',li)

    for op in opers:
        _op = op[:] # 굳이 deepcopy를 안써도 되는군..  [:]는 얕은 복사 인듯하다.
        _li = li[:]
        for i in _op:
            while i in _li:
                index = _li.index(i)
                calcul = _li[index-1] + _li[index] + _li[index+1]
                num = eval(calcul)
                _li[index] = str(num)
                del _li[index+1]
                del _li[index-1]
        answer.append(_li[0])
    print('answer ', answer)

    return max([abs(int(i)) for i in answer])


print(solution("100-200*300-500+20"))