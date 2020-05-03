from collections import Counter

N = int(input())
*A, = map(int, input().split())

l = Counter([i-A[i] for i in range(N)])
r = Counter([i+A[i] for i in range(N)])

ans = 0
for k, v in l.items():
    ans += v*r[k]
print(ans)
