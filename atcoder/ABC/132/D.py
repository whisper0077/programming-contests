from operator import mul
from functools import reduce


def cmb(n, r):
    if r > n:
        return 0
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


N, K = map(int, input().split())
R = N-K

for i in range(K):
    a = cmb(K-1, i)
    b = cmb(R+1, i+1)
    print((a*b) % (10**9+7))
