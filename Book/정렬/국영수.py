n = int(input())
students = []
for i in range(n):
    name, s1, s2, s3 = input().split()
    students.append((name, int(s1), int(s2), int(s3)))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in students:
    print(s[0])


