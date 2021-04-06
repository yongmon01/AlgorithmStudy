import bisect
import math

n = int(input())
homes = list(map(int, input().split()))
homes.sort()

if n == 1:
    print(0)

else:
    avg = sum(homes) / n
    first = math.ceil(avg)
    second = math.floor(avg)

    print(second)
    second_front_index = bisect.bisect_left(homes, second) - 1
    second_rear_index = bisect.bisect_left(homes, second)
    print(second_front_index, second_rear_index)

    print(first)
    first_front_index = bisect.bisect_left(homes, first) - 1
    first_rear_index = bisect.bisect_left(homes, first)
    print(first_front_index, first_rear_index)

    candidates = [homes[second_front_index],homes[second_rear_index],homes[first_front_index],homes[first_rear_index]]
    answer = 0
    mins = int(1e9)
    for i in candidates[::-1]:
        sums = 0
        for j in range(len(homes)):
            sums += abs(homes[j]-i)
        if sums <= mins:
            answer = i
            mins = sums
    print(answer)

# li = [1,5,7,9]
# print(bisect.bisect_left(li,2))
