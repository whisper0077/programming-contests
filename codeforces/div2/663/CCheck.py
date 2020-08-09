import itertools
from collections import deque
*P, = map(int, input().split())
for p in itertools.permutations(P):
    n = len(p)
    a = []
    for i in range(n):
        for j in range(i-1, -1, -1):
            if p[j] > p[i]:
                a.append((j, i))
                break
    for i in range(n):
        for j in range(i+1, n):
            if p[j] > p[i]:
                a.append((j, i))
                break

    c = "x"
    if len(a) < n:
        c = "o"
    print(c, *p)
