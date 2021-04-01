import time
import heapq
def solution(N, coffee_times):
    answer = []
    while len(coffee_times) > N:
        # time.sleep(1)
        min_time = min(coffee_times[:N])
        current_answer = []
        for i in range(N,-1,-1):
            if coffee_times[i] == min_time:
                current_answer.append(i)
                coffee_times.remove(coffee_times[i])
        #print(current_answer)
        #print(current_answer[::-1])
        # answer.append(current_answer[::-1])
        for i in current_answer[::-1]:
            answer.append(i)

        # for i in range(2, -1, -1):
        #     # print(coffee_times[i])
        #     if coffee_times[i] == min_time:
        #         del coffee_times[i]
        #         answer.append(i)
        #     print(coffee_times)
        # print(min_time)
        # print(coffee_times[:3])

    rest_coffee = []
    print(coffee_times)
    for i in range(N):
        heapq.heappush(rest_coffee, (coffee_times[i], i))
    rest_coffee.sort()
    for j in rest_coffee:
        answer.append(j[1])

    return answer
print(solution(3,[4, 2, 2, 5, 3]))
