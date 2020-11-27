n = 2
number = 12

def solution(N, number):
    if N == number:
        return 1
    possible_list = [{}, {N}]
    for i in range(2, 9):
        new_set = {int(str(N) * i)}
        for j in range(1, i//2+1):
            for p in possible_list[j]:
                for q in possible_list[i-j]:
                    new_set.add(p + q)
                    new_set.add(p - q)
                    new_set.add(q - p)
                    new_set.add(p * q)
                    if q != 0:
                        new_set.add(p // q)
                    if p != 0:
                        new_set.add(q // p)
        if number in new_set:
            return i
        possible_list.append(new_set)
    return -1

print(solution(2,11))
print(solution(5,12))
