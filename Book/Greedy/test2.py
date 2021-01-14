# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split(' ')))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort() # 이진 탐색 수행을 위해 정렬 수행

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while (start <= end):
    mid = (start + end) // 2
    count = 1
    value = array[0]

    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)