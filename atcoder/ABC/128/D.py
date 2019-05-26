import heapq
import copy

N, K = map(int, input().split())
*V, = map(int, input().split())

M = min(N, K)

ans = 0
for i in range(M + 1):
    for j in range(M - i + 1):
        l = V[:i] + V[N - 1:N - j - 1:-1]
        t = sum(l)
        l.sort()
        for n in range(min(K - i - j, len(l))):
            if l[n] >= 0:
                break
            t -= l[n]
        if t > ans:
            ans = t

print(ans)