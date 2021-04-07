n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
built = []
# 0 기둥 1 보
i = 0
for build in build_frame:
    i += 1
    print(i,': build_frame',build)
    # a0 기둥 a1 보 b0 삭제 b1 설치
    x, y, a, b = build[0], build[1], build[2], build[3]

    if a == 0 and b == 1:
        if y == 0 or [x-1, y, 1] in built or [x, y-1, 0] in built:
            built.append([x, y, 0])
    elif a == 1 and b == 1:
        if [x, y-1, 0] in built or [x+1, y-1, 0] in built or ([x-1, y, 1] in built and [x+1, y, 1] in built):
            built.append([x, y, 1])
    elif a == 0 and b == 0:
        if [x-1, y, 1] not in built and [x, y, 1] not in built and [x, y-1, 0] not in built:
            continue
        else:
            built.remove([x, y, a])
    elif a == 1 and b == 0:
        if [x+1, y, 0] in built and [x+1, y-1, 0] not in built:
            continue
        elif [x, y, 0] in built and [x, y-1, 0] not in built:
            continue
        elif [x-1, y, 1] in built and [x-1, y-1, 0] not in built:
            continue
        elif [x+1, y, 1] in built and [x+1, y-1, 0] not in built:
            continue
        else:
            built.remove([x, y, a])

    print(built)

built.sort()

print(built)

# def make_build(build_frame):
#
#     result = []
#     for build in build_frame:
#
#         copy_result = []
#         for i in result:
#             copy_result.append(i)
#         x, y = build[0], build[1]
#         delete_or_append = build[3]
#         gidung_or_bo = build[2]
#
#         if delete_or_append == 0:
#             copy_result.remove((x, y, gidung_or_bo))
#         elif delete_or_append == 1:
#             copy_result.append((x, y, gidung_or_bo))
#         if is_okay(copy_result) == True:
#             result = copy_result
#         #print(result)
#     return result
#
#
# def is_okay(result):
#     for i in result:
#         x, y, gidung_or_bo = i[0], i[1], i[2]
#         if gidung_or_bo == 0:
#             if y == 0:
#                 continue
#             elif (x-1, y, 1) in result:
#                 continue
#             elif (x, y, 1) in result:
#                 continue
#             elif (x, y-1, 0) in result:
#                 continue
#             return False
#         elif gidung_or_bo == 1:
#             if (x, y-1, 0) in result:
#                 continue
#             elif (x+1, y-1, 0) in result:
#                 continue
#             elif (x-1, y, 1) in result and (x+1, y, 1) in result:
#                 continue
#             return False
#     return True
#
# def solution(n, build_frame):
#     answer = make_build(build_frame)
#     answer.sort(key= lambda x: (x[0], x[1], x[2]))
#     answer = list(map(list, answer))
#     return answer