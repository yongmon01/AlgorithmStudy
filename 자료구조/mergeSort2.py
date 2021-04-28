# 머지소트 top down 하향식 return 없는 식.

# 병합 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)
def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1) # 재귀 호출로 첫 번째 그룹을 정렬
    merge_sort(g2) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합

    merge(a, g1, g2)

def merge(a, g1, g2):
    i1 = 0
    i2 = 0
    ia = 0
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


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
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