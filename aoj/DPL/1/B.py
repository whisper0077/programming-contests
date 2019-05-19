N, W = map(int, input().split())
vw = [[0, 0]]+[list(map(int, input().split())) for _ in range(N)]
'''
ナップザック問題
i番目までの品物で作れる価値の最大値を求めていく
'''
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(W+1):
        v = dp[i-1][j]
        if j >= vw[i][1]:
            t = dp[i-1][j-vw[i][1]] + vw[i][0]
            if t > v:
                v = t
        dp[i][j] = v
print(dp[N][W])
