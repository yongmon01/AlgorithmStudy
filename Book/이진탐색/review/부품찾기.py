n = int(input())
have = list(map(int, input().split()))
m = int(input())
need = list(map(int, input().split()))

for i in need:
    if i in have:
        print('YES', end=' ')
    else:
        print('NO', end=' ')


