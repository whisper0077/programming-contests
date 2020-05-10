from collections import defaultdict


def nC2(n):
    if n < 2:
        return 0
    return n*(n-1)//2


N = int(input())
*A, = map(int, input().split())

h = defaultdict(int)
for a in A:
    h[a] += 1

total = 0
for k, v in h.items():
    total += nC2(v)

for k in range(N):
    t = A[k]
    print(total - h[t] + 1)
