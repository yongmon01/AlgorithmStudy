n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)

second = m // (k+1)
first = m - second

print(num_list)

print(num_list[0] * first + num_list[1] * second)