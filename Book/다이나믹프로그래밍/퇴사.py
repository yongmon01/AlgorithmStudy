n = int(input())
t = [0] * n
p = [0] * n
for i in range(n):
    t[i], p[i] = map(int, input().split())
print(t, p)

def good(index, earn):
    if index >= n:
        return earn
    if index + t[index] > n:
        return good(index + 1, earn)
    return max(good(index + t[index], earn + p[index]), good(index + 1, earn))

print(good(0, 0))

# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200