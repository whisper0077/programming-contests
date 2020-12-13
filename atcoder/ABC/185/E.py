N, M = map(int, input().split())
*A, = map(int, input().split())
*B, = map(int, input().split())

dp = [[10**9 for j in range(M+1)] for i in range(N+1)]
dp[0][0] = 0

for i in range(N+1):
    for j in range(M+1):
        if i < N:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
        if j < M:
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
        if i < N and j < M:
            dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+(A[i] != B[j]))
'''
もらうDP
dp = [[max(i, j) for j in range(M+1)] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = min(
            dp[i-1][j-1]+(A[i-1] != B[j-1]),
            dp[i-1][j]+1,
            dp[i][j-1]+1
        )
'''

print(dp[N][M])
