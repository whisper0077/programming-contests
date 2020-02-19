wps = [
    [3000000000, 2], [4000000000, 3], [1000000000, 2], [2000000000, 3], [3000000000, 6]
]
N = 5
W = 10**10
P = sum([v[1] for v in wps])


def dp():
    dp = [[W+1]*(P+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(P+1):
            wp = wps[i-1]
            if (j-wp[1]) < 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min([dp[i-1][j], dp[i-1][j-wp[1]]+wp[0]])
    r = 0
    for i in range(P+1):
        if dp[N][i] <= W:
            r = i
    return r


print(dp())
