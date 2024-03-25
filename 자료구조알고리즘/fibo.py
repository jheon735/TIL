def solution(x):
    return fibo_ite(x)


def fibo_rec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo_rec(x - 1) + fibo_rec(x - 2)


def fibo_ite(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    f1 = 0
    f2 = 1
    for i in range(x - 1):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    return f2