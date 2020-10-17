N = int(input())
xyz = [list(map(int, input().split())) for _ in range(N)]
d = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        a, b, c = xyz[i]
        p, q, r = xyz[j]
        d[i][j] = abs(p-a)+abs(q-b)+max(0, r-c)
        d[j][i] = abs(a-p)+abs(b-q)+max(0, c-r)

dp = [[float('inf')]*N for _ in range(2**N)]
dp[0][0] = 0

# bitDP
for s in range(2**N):
    for u in range(N):
        for v in range(N):
            if s & (1 << v) == 0:
                dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v], dp[s][u]+d[u][v])

print(dp[2**N-1][0])
