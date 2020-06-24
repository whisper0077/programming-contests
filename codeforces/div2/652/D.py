M = 10**9+7
dp = [0]*(2*10**6+1)
dp[1] = 0
dp[2] = 0
dp[3] = 1
for i in range(4, len(dp)):
    d = dp[i-2]*2 % M
    d = (d+dp[i-1]) % M
    if i % 3 == 0:
        d += 1
    dp[i] = d

for t in range(int(input())):
    n = int(input())
    print(dp[n]*4 % M)
