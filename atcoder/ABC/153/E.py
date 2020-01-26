H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [10**9]*(H+1)
dp[0] = 0

for i in range(1, N+1):
    for j in range(H+1):
        a, b = ab[i-1]
        if j < a:
            dp[j] = min([dp[0]+b, dp[j]])
        else:
            dp[j] = min([dp[j-a]+b, dp[j]])
print(dp[H])
