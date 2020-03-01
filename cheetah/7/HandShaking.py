
def countPerfect(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i in range(4, n+1, 2):
        # 時計回りに1人飛ばしで偶数組を作っていく
        for j in range(1, n+1, 2):
            dp[i] += dp[j-1] * dp[i-(j-1)-2]
    return dp[n]


q = [2, 4, 6, 8, 32]
for v in q:
    print(countPerfect(v))
