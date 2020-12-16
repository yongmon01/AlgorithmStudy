build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def make_build(build_frame):

    result = []
    for build in build_frame:

        copy_result = []
        for i in result:
            copy_result.append(i)
        x, y = build[0], build[1]
        delete_or_append = build[3]
        gidung_or_bo = build[2]

        if delete_or_append == 0:
            copy_result.remove((x, y, gidung_or_bo))
        elif delete_or_append == 1:
            copy_result.append((x, y, gidung_or_bo))
        if is_okay(copy_result) == True:
            result = copy_result
    return result

def is_okay(result):
    for i in result:
        x, y, gidung_or_bo = i[0], i[1], i[2]
        if gidung_or_bo == 0:
            if y == 0:
                continue
            elif (x-1, y, 1) in result:
                continue
            elif (x, y, 1) in result:
                continue
            elif (x, y-1, 0) in result:
                continue
            return False
        elif gidung_or_bo == 1:
            if (x, y-1, 0) in result:
                continue
            elif (x+1, y-1, 0) in result:
                continue
            elif (x-1, y, 1) in result and (x+1, y, 1) in result:
                continue
            return False
    return True

answer = make_build(build_frame)
answer.sort(key= lambda x: (x[0], x[1], x[2]))
answer = list(map(list, answer))
print(answer)