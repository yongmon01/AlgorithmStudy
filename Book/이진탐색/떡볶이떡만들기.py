import sys

n, m = map(int, input().split())
dducks = list(map(int, sys.stdin.readline().rstrip().split()))
dducks.sort(reverse=True)
total = 0
length = dducks[0]

while total < m:
    total = 0
    length -= 1
    for dduck in dducks:
        if dduck > length:
            total += (dduck - length)
        else:
            break

print(length)