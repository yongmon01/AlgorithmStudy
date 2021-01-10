n = int(input())

d = [0] * 1000
d[1], d[2] = 1, 3
for i in range(2, n):
    d[i] = d[n-1] + d[n-2] * 2
print(d)
print(d[n])