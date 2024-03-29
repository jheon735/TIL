import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True: #log(n)
        min1 = heapq.heappop(scoville)  #O(log n)
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        min2 = heapq.heappop(scoville)  #O(log n)
        newfood = min1 + 2*min2
        heapq.heappush(scoville, newfood)   #O(log n)
        answer += 1

    return answer