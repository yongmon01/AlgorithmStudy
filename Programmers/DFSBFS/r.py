from collections import deque
def solution(tickets):
    path = len(tickets)
    answer = ["ICN"]
    dictionary = {}
    for depart, dest in tickets:
        if depart in dictionary:
            dictionary[depart].append(dest)
        else:
            dictionary[depart] = [dest]

    for i in dictionary:
        dictionary[i].sort(reverse=True)

    print(dictionary)

    q, last = deque(['ICN']), ""
    while path > 0:
        station = dictionary[q[-1]][-1]
        del dictionary[q[-1]][-1]
        q.append(station)
        path -= 1
        print(q)
        # print(path != 0)
        # print(station not in dictionary)
        # print(station in dictionary and len(dictionary[station]))
        print(path != 0) and ((station not in dictionary) or (station in dictionary and len(dictionary[station]) == 0))
        if (path != 0) and ((station not in dictionary) or (station in dictionary and len(dictionary[station]) == 0)):
            last = q.pop()

    if last != "":
        q.append(last)

    return list(q)


tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]
print(solution(tickets))


# def solution(tickets):
#     answer = ["ICN"]
#     dictionary = {}
#     for deprt, destn in tickets:
#         if deprt in dictionary:
#             dictionary[deprt].append(destn)
#         else:
#             dictionary[deprt] = [destn]
#
#     for i in dictionary:
#         dictionary[i].sort(reverse=True)
#
#     print(dictionary)
#
#     depart = "ICN"
#     while len(dictionary[depart]) != 0:
#         next_station = dictionary[depart][-1]
#         if next_station not in dictionary and len(dictionary[depart]) >= 2:
#             next_station = dictionary[depart][-2]
#         elif next_station not in dictionary:
#             answer.append(next_station)
#             break
#         elif next_station in dictionary and len(dictionary[next_station]) == 0:
#             next_station = dictionary[depart][-2]
#         # del dictionary[depart][-1]
#         dictionary[depart].remove(next_station)
#         answer.append(next_station)
#         depart = next_station
#
#         # if depart not in dictionary:
#         #     break
#
#     return answer
#
# print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]))