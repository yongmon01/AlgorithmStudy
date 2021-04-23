n = int(input())
numbers = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())
answer = []

def dfs(numbers, i, val):
    global plus, sub, mul, div
    print(i)
    print(val)
    if i == len(numbers):
        answer.append(val)

    if plus > 0:
        plus -= 1
        dfs(numbers, i+1, val + numbers[i])
        plus += 1
    if sub > 0:
        sub -= 1
        dfs(numbers, i+1, val - numbers[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(numbers, i+1, val * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        if val > 0:
            dfs(numbers, i+1, val//numbers[i])
        if val < 0:
            val = -val
            curr = val//numbers[i]
            dfs(numbers, i+1, -curr)
        # dfs(numbers, i+1, int(val/numbers[i]))
        div += 1

dfs(numbers, 1, numbers[0])
print(answer)
print(max(answer))
print(min(answer))

# 6
# 1 2 3 4 5 6
# 2 1 1 1

# print(numbers)
# print(plus, sub, mul, div)