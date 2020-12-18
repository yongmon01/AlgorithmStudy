n = int(input())
students = []
for i in range(n):
    name_and_score = input().split()
    students.append((name_and_score[0], int(name_and_score[1])))
students.sort(key=lambda x: x[1])
for i in students:
    print(i[0], end=' ')

