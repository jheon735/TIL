def solution(N, number):
    sets = [set() for i in range(8)]
    for i, x in enumerate(sets, start=1):
        x.add(int(str(N) * i))
    for i in range(1, len(sets)):
        for j in range(i):
            for op1 in sets[j]:
                for op2 in sets[i - j - 1]:
                    sets[i].add(op1 + op2)
                    sets[i].add(op1 - op2)
                    sets[i].add(op1 * op2)
                    if op2 != 0:
                        sets[i].add(op1 // op2)
        if number in sets[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

print(solution(5, 5))