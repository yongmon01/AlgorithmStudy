import bisect

n = int(input())
numbers = list(map(int, input().split()))

dp_in = [1] * n
dp_de = [1] * n

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_in[i] = max(dp_in[i], dp_in[j]+1)

numbers = numbers[::-1]
for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp_de[i] = max(dp_de[i], dp_de[j]+1)
dp_de = dp_de[::-1]

print(dp_in)
print(dp_de)
new_dp = []
for i in range(n):
    new_dp.append(dp_de[i] + dp_in[i])
print(new_dp)
