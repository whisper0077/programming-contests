N, K = map(int, input().split())
*a, = map(int, input().split())
MOD = 10**9+7

dp = [0]*(K+1)
sums = [0]*(K+2)

dp[0] = 1

for i in range(1, N+1):
    sums[0] = 0
    for j in range(1, K+2):
        sums[j] = (dp[j-1]+sums[j-1]) % MOD

    for j in range(1, K+1):
        sj = max([0, j-a[i-1]])
        dp[j] = (sums[j+1]-sums[sj]+MOD) % MOD
print(dp[K])
