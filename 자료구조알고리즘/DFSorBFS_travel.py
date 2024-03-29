def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []).append([t[1]])
    for r in routes:    #O(nlogn) 이곳이 지배
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:   #O(n)
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top].pop()

    return path[::-1]


def solution2(tickets):
    ways = {}
    for ticket in tickets:
        ways[ticket[0]] = ways.get(ticket[0], []) + [ticket[1]]
    for way in ways:
        ways[way].sort(reverse=True)
    stack = ["ICN"]
    answer = []
    while stack:
        now = stack[-1]
        if now in ways and len(ways[now]) != 0:
            stack.append(ways[now].pop())
        else:
            answer.append(stack.pop())

    return answer[::-1]

print(solution2([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))