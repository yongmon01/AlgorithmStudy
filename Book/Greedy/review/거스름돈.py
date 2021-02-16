n = int(input())
coin = [500,100,50,10]
count = 0

for c in coin:
    count += n // c
    n %= c

print(count)