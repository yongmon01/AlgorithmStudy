import time
import heapq
def solution(N, coffee_times):
    answer = []
    #시간, 인덱스
    coffee_times= [(coffee_times[i], i) for i in range(len(coffee_times))]
    print('..?',coffee_times)
    while len(coffee_times) > N:
        # time.sleep(1)
        min_time = min(coffee_times[:N])[0]
        current_answer = []
        for i in range(N-1,-1,-1):
            print(i)
            if coffee_times[i][0] == min_time:
                current_answer.append(coffee_times[i][1])
                coffee_times.remove(coffee_times[i])
            else:
                update_time = coffee_times[i][0] - min_time
                coffee_times[i] = (update_time, i)
            print('..',coffee_times)
        #print(current_answer)
        #print(current_answer[::-1])
        # answer.append(current_answer[::-1])
        for i in current_answer[::-1]:
            answer.append(i)

    print(coffee_times)
    coffee_times.sort()
    print(coffee_times)
    for i in coffee_times:
        answer.append(i[1])
    for i in range(len(answer)):
        answer[i] += 1

    return answer
print(solution(3,[4,2]))
