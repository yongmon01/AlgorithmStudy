def get_distance(a,b,li):
    answer = abs(li[a][0]-li[b][0]) + abs(li[a][1]-li[b][1])
    return answer

def solution(numbers, hand):
    li = [-1,(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,2)]
    answer = ''
    left, right = 10, 12
    new_numbers = []
    for i in numbers:
        if i == "*":
            new_numbers.append(10)
        elif i == 0:
            new_numbers.append(11)
        elif i == "#":
            new_numbers.append(12)
        else:
            new_numbers.append(i)
    print(new_numbers)
    for i in new_numbers:
        if i == 1 or i == 4 or i == 7 or i == 10:
            left = i
            answer += 'L'
        elif i == 3 or i == 6 or i == 9 or i == 12:
            right = i
            answer += 'R'
        else:
            d_left = get_distance(left, i, li)
            d_right = get_distance(right, i, li)
            if d_left == d_right:
                if hand == "right":
                    right = i
                    answer += 'R'
                else:
                    left = i
                    answer += 'L'
            elif d_left < d_right:
                left = i
                answer += 'L'
            else:
                right = i
                answer += 'R'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #
