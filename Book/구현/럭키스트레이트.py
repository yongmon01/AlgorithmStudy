score = input()
# 6 /0 1 2/ 3 4 5
first_half = score[0:(len(score)//2)]
second_half = score[(len(score)//2):]

first_sum, second_sum = 0, 0

for i in first_half:
    first_sum += int(i)
for i in second_half:
    second_sum += int(i)

if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")
