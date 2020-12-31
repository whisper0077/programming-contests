from collections import defaultdict, deque
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    *w, = map(int, input().split())
    c = [0]*n
    for i in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        c[u] += 1
        c[v] += 1

    l = []
    for i in range(n):
        if c[i] > 1:
            l += [w[i]]*(c[i]-1)
    l.sort(reverse=True)

    ans = [sum(w)]
    for i in range(n-2):
        ans.append(ans[-1]+l[i])
    print(*ans)
