N, A = map(int, input().split())
*x, = map(int, input().split())
l = N * A + 1

# dp[n枚選ぶ][m枚目まで][総和]
dp = [[[0] * l for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for n in range(0, N + 1):
    for m in range(N):
        for s in range(0, l):
            dp[n][m + 1][s] += dp[n][m][s]
            if s >= x[m]:
                dp[n][m + 1][s] += dp[n - 1][m][s - x[m]]

print(sum([dp[n][N][n * A] for n in range(1, N + 1)]))