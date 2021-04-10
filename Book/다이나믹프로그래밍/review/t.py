n = int(input())
t=[0]*n;p=[0]*n
for i in range(n):
    t[i],p[i]=map(int,input().split())
d = [0]*(n+1)
for i in range(n+1):
    print(d)
    for j in range(i):
        if j+t[j] <= i and d[j] + p[j] >= d[i]:
            d[i] = d[j] + p[j]
print(d[n])