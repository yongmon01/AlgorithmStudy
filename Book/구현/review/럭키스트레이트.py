n = input()
n = str(n)

first = n[0: len(n)//2]
second = n[len(n)//2:]

sum = 0
for i in first:
    sum += int(i)
for i in second:
    sum -= int(i)

if sum == 0:
    print('LUCKY')
else:
    print('READY')