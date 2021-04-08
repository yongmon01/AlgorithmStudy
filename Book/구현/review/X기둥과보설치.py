n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
built = []

def is_okay(built):
    for build in built:
        p, q, r = build[0], build[1], build[2]
        if r == 0:
            if not (q == 0 or (p-1, q, 1) in built or (p, q, 1) in built or (p, q-1, 0) in built):
                return False
        if r == 1:
            if not ((p, q-1, 0) in built or (p+1, q-1, 0) in built or ((p-1, q, 1) in built and (p+1, q, 1) in built)):
                return False
    return True

# 0 기둥 1 보
for build in build_frame:

    # a0 기둥 a1 보 b0 삭제 b1 설치
    x, y, a, b = build[0], build[1], build[2], build[3]
    if b == 1:
        built.append((x, y, a))
        if not is_okay(built):
            built.remove((x, y, a))
    elif b == 0:
        built.remove((x, y, a))
        if not is_okay(built):
            built.append((x, y, a))

built.sort()
print(built)