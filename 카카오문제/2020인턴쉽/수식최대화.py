# 장하다...풀었다..

from itertools import permutations
from copy import deepcopy

def calcul(a, b, c):
    if c == '*':
        return a * b
    elif c == '-':
        return a - b
    elif c == '+':
        return a + b

def solution(expression):
    answers = []

    expression += '-' # 숫자와 연산자 구분을 위해 그냥 끝에 - 붙여줌. 밑에 for문 보면암.
    answer = 0
    oper = ['*', '+', '-']
    orders = list(permutations(oper, 3))
    print('!', orders)
    solid_nums = []
    solid_chars = []

    # 숫자와 연산자 나눠서 배열에 각각 넣음.
    tmp = ''
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            solid_nums.append(int(tmp))
            tmp = ''
            solid_chars.append(i)

    del solid_chars[-1] # 17번째줄에 넣어준 "-" 는 삭제함.
    print('solid_nums', solid_nums)
    print('chars', solid_chars)


    for p in range(len(orders)):
        order = orders[p]
        nums = deepcopy(solid_nums) # 카피해야 for문 돌때 정상적으로 원하는 계산이됨.
        chars = deepcopy(solid_chars) # 여기도.

        for i in range(3):
            print(nums)
            turn = order[i]
            for j in range(len(chars)):
                if chars[j] == turn:
                    nums[j+1] = calcul(nums[j], nums[j+1], turn)
                    nums[j] = 'X'
                    chars[j] = 'X'
            for k in range(len(chars)-1, -1, -1):
                if nums[k] == 'X':
                    del nums[k]
                if chars[k] == 'X':
                    del chars[k]

        print(nums)
        answers.append(nums[0])

    answers = [abs(i) for i in answers]
    return answers

print(solution("100-200*300-500+20"))
