import bisect
N, K = map(int, input().split())
*a, = map(int, input().split())
s = [0]*N
s[0] = a[0]
for i in range(1, N):
    s[i] = s[i-1]+a[i]

ans = 0
for i in range(N):
    t = s[i]+K-a[i]
    ti = bisect.bisect_left(s, t)
    ti = min(ti, N-1)
    if (s[ti]-s[i]+a[i]) >= K:
        ans += N-ti

print(ans)
