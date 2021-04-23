from bisect import bisect_left
# 5457
# 3
# 6 7 8

def dfs(numbers, i, current,target):
    print(current)
    if i == len(target):
        answer.append(current)
        return
    index = bisect_left(numbers, int(target[i]))
    print('index',index)
    dfs(numbers, i+1, current + str(numbers[index-1]), target)
    dfs(numbers, i+1, current + str(numbers[index]), target)

target = input()
n = int(input())
numbers = [i for i in range(10)]
broken = list(map(int, input().split()))
for i in broken:
    numbers.remove(i)

# if n == 9:


answer = []
dfs(numbers, 0, "",target)
print(answer)

answer2 = []
for i in answer:
    answer2.append(abs(int(i)-int(target))+len(i))
print(answer2)

nogada = abs(int(target)-100)
min_num = min(answer2)
if min_num < nogada:
    print(min_num)
else:
    print(nogada)
