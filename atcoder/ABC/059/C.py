import copy
n = int(input())
*A, = map(int, input().split())


def solve(p):
    r = 0
    t = 0
    for a in A:
        t += a
        if t * p <= 0:
            r += abs(p - t)
            t = p
        p *= -1
    return r


print(min(solve(1), solve(-1)))
