import sys
sys.setrecursionlimit(10**8)

# ナップザック問題 典型2
N, W = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(N)]
V = sum([v for w, v in wv])

dp = [[10**10]*(V+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(0, V+1):
        w, v = wv[i]
        if (j-v) >= 0:
            dp[i+1][j] = min([dp[i][j], dp[i][j-v]+w])
        else:
            dp[i+1][j] = dp[i][j]

ans = 0
for i in range(0, V+1):
    if dp[N][i] <= W:
        ans = i

print(ans)
