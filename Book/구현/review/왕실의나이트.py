index_x = [1,2,3,4,5,6,7,8]
index_y = ['a','b','c','d','e','f','g','h']
p = input()
x, y = p[1], p[0]
y = index_y.index(y) + 1
x, y = int(x), int(y)
# print(x, y)
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count)

print(ord('b'))
