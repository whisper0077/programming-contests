H, W = 5, 4


def dfs(h, w):
    if h > H or w > W:
        return 0
    if h == H and w == W:
        return 1
    r = dfs(h, w+1)+dfs(h+1, w)
    return r


memo = [[0]*W for h in range(H)]


def dfsmemo(h, w):
    if h > H or w > W:
        return 0
    if h == H and w == W:
        return 1
    if memo[h][w] > 0:
        return memo[h][w]
    memo[h][w] = dfs(h, w+1)+dfs(h+1, w)
    return memo[h][w]


def dp():
    dp = [[0]*(W+1) for h in range(H+1)]
    dp[0][0] = 1
    for h in range(H+1):
        for w in range(W+1):
            if h > 0:
                dp[h][w] += dp[h-1][w]
            if w > 0:
                dp[h][w] += dp[h][w-1]
    return dp[H][W]


print(dfs(0, 0))
print(dfsmemo(0, 0))
print(dp())
