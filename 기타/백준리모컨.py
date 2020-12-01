# 5457  3  6,7,8

target = input()
n = int(input())
numbers = [0,1,2,3,4,5,6,7,8,9]
broken_numbers = list(map(int, input().split()))
for i in broken_numbers:
    numbers.remove(i)
return_number_list = []

def return_near_number(n, numbers):
    if n in numbers:
        return [n]
    else:
        numbers.append(n)
        numbers.sort()
        index_n = numbers.index(n) #
        first, second = numbers[index_n-1], numbers[index_n +1]
        numbers.remove(n) #
        return [first, second]


curr_nums = return_near_number(int(target[0]), numbers)
print(curr_nums)
for j in curr_nums:
    return_number_list.append(str(j))

new_target = target[1:]

for i in new_target:
    curr_nums = return_near_number(int(i), numbers)
    new_list = []
    for j in return_number_list:
        for k in curr_nums:
            new = j + str(k)
            new_list.append(new)
    return_number_list = new_list

print(return_number_list, " return_number_list")

answer_list = []
for i in return_number_list:
    print("abs((int(i) - int(target)) ", abs(int(i) - int(target)) , " len(i) ", len(i))
    append_number = abs(int(i) - int(target)) + len(i)
    print(append_number, ' append_number')
    answer_list.append(append_number)
answer_list.append(abs(100-int(target)))

print(answer_list)
print(min(answer_list))





# enable = {str(i) for i in range(10)}  # 0, 1, 2 ... 9 (가능한 수)
#
# # input
# N = int(input())  # 이동하려고 하는 채널
# M = int(input())  # 고장난 버튼의 개수
# if M != 0:
#     enable -= set(map(str, input().split()))  # 고장난 버튼 리스트 제거
# print(enable)
#
# # case1 (100번에서 +, - 로만 움직이는 경우)
# min_cnt = abs(100 - N)
#
# # case2 (1,000,000 채널까지 브루트 포스 진행)
# # 500,000 채널까지 존재하기 때문에 500,000 보다 크면서 모든 숫자의 경우를 거치는 1,000,000까지를 범위로 잡음
# for num in range(1000001):
#     num = str(num)
#     for j in range(len(num)):
#         if num[j] not in enable:
#             break
#         elif j == len(num) - 1:
#             min_cnt = min(min_cnt, abs(N - int(num)) + len(str(num)))
# print(min_cnt)