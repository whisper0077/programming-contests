INF = 10**10
N = int(input())
c = [1]
for i in range(1, 20):
    if 6**i <= N:
        c.append(6**i)
    if 9**i <= N:
        c.append(9**i)

dp = [INF]*(N+1)
dp[0] = 0
for i in range(len(c)):
    for k in range(N+1):
        if (k-c[i]) >= 0:
            dp[k] = min(dp[k], dp[k-c[i]]+1)

print(dp[-1])
