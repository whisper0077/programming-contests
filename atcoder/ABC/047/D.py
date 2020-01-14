from collections import defaultdict

N, T = map(int, input().split())
*a, = map(int, input().split())
t = defaultdict(int)
m = a[0]
p = 0
ans = 0
for i in range(1, N):
    c = a[i] - m
    if t[m] < c:
        t[m] = c
    if a[i] < m:
        m = a[i]
    if c > p:
        p = c
        ans = 1
    elif c == p:
        ans += 1

print(ans)
