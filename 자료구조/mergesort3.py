# 머지소트 bottom up 상향식 return 없는 식. 하...

# 병합 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return

    # i개 씩 묶는것
    i = 1
    while i < len(a):
        print('i ',i)
        j = 0
        while j < len(a):
            # if j + i > len(a): 없어도 됨.
            #     break
            merge(a, i, j)
            print(j, j+i, j +i+i)
            print(a)
            j += i + i
        i += i

    # 두 그룹을 하나로 병합


def merge(a, i, j):
    g1 = a[j: j+i]
    g2 = a[j+i : j+i+i]
    i1 = 0
    i2 = 0
    ia = j
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    # 아직 남아 있는 자료들을 결과에 추가
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1


d = [6, 8, 3, 9, 10, 1, 2, 4] # [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)

d1 = [1, 3, 5, 7, 9, 11, 13, 11]
d2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
d3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
merge_sort(d1)
merge_sort(d2)
merge_sort(d3)
print(d1)
print(d2)
print(d3)




# # 머지소트 bottom up 상향식 return 없는 식.
#
# # 병합 정렬
# # 입력: 리스트 a
# # 출력: 없음(입력으로 주어진 a가 정렬됨)
# def merge_sort(a):
#     n = len(a)
#     # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
#     if n <= 1:
#         return
#
#     # i개 씩 묶는것
#     i = 1
#     while i < len(a):
#         print('i ',i)
#         j = 0
#         while j < len(a):
#             if j + i > len(a):
#                 break
#             merge(a[j:j+i+i], a[j:j+i], a[j+i:j+i+i])
#             print(j, j+i, j +i+i)
#             print(a)
#             j += i + i
#         i += i
#
#     # 두 그룹을 하나로 병합
#
#
# def merge(a, g1, g2):
#     i1 = 0
#     i2 = 0
#     ia = 0
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] < g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
#      # 아직 남아 있는 자료들을 결과에 추가
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1
#
#
# d = [6, 8, 3, 9, 10, 1, 2, 4] # [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
# merge_sort(d)
# print(d)
#
# # d1 = [1, 3, 5, 7, 9, 11, 13, 11]
# # d2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
# # d3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
# # merge_sort(d1)
# # merge_sort(d2)
# # merge_sort(d3)
# # print(d1)
# # print(d2)
# # print(d3)



# c = int(input())
# numbers = []
# for i in range(c):
#     numbers.append(int(input()))
#
# def merge_sort(a):
#     n = len(a)
#
#     if n <= 1:
#         return
#
#     i = 1
#     while i < len(a):
#         j = 0
#         while j < len(a):
#             if j + i > len(a):
#                 break
#             merge(a, i, j)
#             j += i + i
#         i += i
#
# def merge(a, i, j):
#     g1 = a[j: j+i]
#     g2 = a[j+i : j+i+i]
#     i1 = 0
#     i2 = 0
#     ia = j
#     while i1 < len(g1) and i2 < len(g2):
#         if g1[i1] < g2[i2]:
#             a[ia] = g1[i1]
#             i1 += 1
#             ia += 1
#         else:
#             a[ia] = g2[i2]
#             i2 += 1
#             ia += 1
#     # 아직 남아 있는 자료들을 결과에 추가
#     while i1 < len(g1):
#         a[ia] = g1[i1]
#         i1 += 1
#         ia += 1
#     while i2 < len(g2):
#         a[ia] = g2[i2]
#         i2 += 1
#         ia += 1
#
# merge_sort(numbers)
# for i in numbers:
#     print(i)