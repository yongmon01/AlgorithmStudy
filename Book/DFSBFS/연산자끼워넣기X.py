n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_num = -1e9
min_num = 1e9

def dfs(i, num):
    global max_num, min_num, add, sub, mul, div

    if i == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
        # return
    else:
        if add > 0:
            add -= 1
            dfs(i+1, num + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, num - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, num * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, -int(-num // numbers[i]))
            div += 1

dfs(1, numbers[0])
print(max_num)
print(min_num)
