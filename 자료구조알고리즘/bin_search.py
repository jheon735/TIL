def solution(L, x):
    left = 0
    right = len(L) - 1

    while right >= left:
        cent = left + (right - left) // 2
        if L[cent] == x:
            return cent
        elif L[cent] < x:
            left = cent + 1
        else:
            right = cent - 1

    return -1