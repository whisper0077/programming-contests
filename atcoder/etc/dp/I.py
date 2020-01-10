N = int(input())
*p, = map(float, input().split())

dp = [[0]*(N+1) for i in range(N+1)]
dp[0][0] = 1.0

for i in range(N):
    for j in range(i+1):
        dp[i+1][j+1] += dp[i][j]*p[i]
        dp[i+1][j] += dp[i][j]*(1.0-p[i])

ans = sum([dp[N][i] for i in range((N+1)//2, N+1)])
print(ans)

'''
確率DP
http://compro.tsutajiro.com/archive/180220_probability_dp.pdf
'''
