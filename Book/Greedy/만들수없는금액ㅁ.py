import itertools
n = int(input())
num_list = list(map(int, input().split()))

possible_numbers = set()

def add_list(tuple_list):
    return_list = []
    for i in tuple_list:
        current_sum = 0
        for j in i:
            current_sum += j
        return_list.append(current_sum)
    return return_list

for i in range(1,n+1):
    current_list = list(itertools.combinations(num_list, i))
    current_possible_numbers = add_list(current_list)
    for j in current_possible_numbers:
        possible_numbers.add(j)

i = 1
while True:
    if i not in possible_numbers:
        print(i)
        break
    i += 1

# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
#
# target = 1
# for x in data:
#     # 만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x
#
# # 만들 수 없는 금액 출력
# print(target)




