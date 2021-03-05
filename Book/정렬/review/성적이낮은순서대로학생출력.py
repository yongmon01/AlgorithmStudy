n = int(input())
li = []
for i in range(n):
    name, score = input().split()
    li.append((int(score), name))
li.sort()

for i in li:
    print(i[1], end=' ')