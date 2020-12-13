N, M = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())

dp = [[max(i, j) for j in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = min(
            dp[i-1][j-1]+(A[i-1] != B[j-1]),
            dp[i-1][j]+1,
            dp[i][j-1]+1
        )

print(dp[N][M])
