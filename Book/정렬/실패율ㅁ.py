from collections import deque
n = 5
stages = [1,2,2,2,3,3,4,6]
answers = []
for i in range(1, n+1):
    count_i = stages.count(i)
    answers.append((i, (count_i/len(stages))))
    for j in range(count_i):
        del stages[0]
answers.sort(key = lambda x:-x[1])
answers = [i[0] for i in answers]

print(answers)