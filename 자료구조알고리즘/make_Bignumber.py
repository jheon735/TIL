def solution(numbers):
    snums = [str(x) for x in numbers]
    snums.sort(key = lambda x : (x*4)[:4], reverse = True)
    if snums[0] == '0':
        return '0'
    else:
        return ''.join(snums)


def solution(number, k):
    answer = []
    for i, num in enumerate(number):
        while len(answer) > 0 and answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
        if k == 0:
            answer.append(number[i:])
            break
        answer.append(num)

    answer = answer[:-k] if k > 0 else answer

    return ''.join(answer)