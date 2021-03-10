n = int(input())
li = list(map(int, input().split()))

d = [0] * (n)
d[0], d[1] = li[0], max(li[0], li[1])

for i in range(2, n):
    d[i] = max(d[i-2] + li[i], d[i-1])

print(d)
print(d[-1])