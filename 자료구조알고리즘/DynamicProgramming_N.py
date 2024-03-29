def solution(N, number):
    s = [set() for x in range(8)]
    for i, x in enumerate(s, start = 1):
        x.add(int(str(N)*i))

    return
