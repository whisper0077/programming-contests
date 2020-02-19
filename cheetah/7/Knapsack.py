
wps = [
    [3, 2], [4, 3], [1, 2], [2, 3], [3, 6]
]
N = 5
M = 10

mm = [[0]*(M+1) for i in range(N)]


def memo(n, w):
    if n >= N:
        return 0
    if mm[n][w] > 0:
        return mm[n][w]
    wp = wps[n]
    r = memo(n+1, w)
    if (w+wp[0]) <= M:
        r = max([r, memo(n+1, w+wp[0]) + wp[1]])
    mm[n][w] = r
    return r


def dp():
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            wp = wps[i-1]
            if (j-wp[0]) < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max([dp[i-1][j], dp[i-1][j-wp[0]]+wp[1]])
    return dp[N][M]


print(memo(0, 0))
print(dp())
