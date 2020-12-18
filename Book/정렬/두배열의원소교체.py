n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    A_min = min(A)
    B_max = max(B)

    if A_min < B_max:
        A.append(B_max)
        A.remove(A_min)
        B.remove(B_max)
    else:
        break

print(sum(A))

