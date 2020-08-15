R, C, K = map(int, input().split())
g = [[-float('inf')]*C for _ in range(R)]
for i in range(K):
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    g[r][c] = k

dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]
for r in range(R):
    for c in range(C):
        # k[0..3] = 0個拾っている状態から3個拾っている状態
        # indexが大きいほど、小さいアイテムとなるので、小さいものから更新していく
        for k in range(2, -1, -1):
            dp[k+1][r][c] = max(
                dp[k+1][r][c],
                dp[k][r][c]+g[r][c]
            )

        for k in range(4):
            dp[0][r+1][c] = max(dp[0][r+1][c], dp[k][r][c])
            dp[k][r][c+1] = max(dp[k][r][c+1], dp[k][r][c])

ans = 0
for i in range(4):
    ans = max(dp[i][R-1][C-1], ans)
print(ans)
