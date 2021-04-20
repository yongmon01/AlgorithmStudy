def solution(tickets):
    answer = ["ICN"]
    dictionary = {}
    for deprt, destn in tickets:
        if deprt in dictionary:
            dictionary[deprt].append(destn)
        else:
            dictionary[deprt] = [destn]

    for i in dictionary:
        dictionary[i].sort(reverse=True)

    print(dictionary)

    depart = "ICN"
    while len(dictionary[depart]) != 0:
        next_station = dictionary[depart][-1]
        if next_station not in dictionary and len(dictionary[depart]) >= 2:
            next_station = dictionary[depart][-2]
        elif next_station not in dictionary:
            answer.append(next_station)
            break
        elif next_station in dictionary and len(dictionary[next_station]) == 0:
            next_station = dictionary[depart][-2]
        # del dictionary[depart][-1]
        dictionary[depart].remove(next_station)
        answer.append(next_station)
        depart = next_station

        # if depart not in dictionary:
        #     break

    return answer

print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]))

# ss = "asv"
# while len(ss) <= 5:
#     print(ss)
#     ss += "b"