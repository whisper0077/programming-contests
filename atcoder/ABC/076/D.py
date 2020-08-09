N = int(input())
*t, = map(int, input().split())
*v, = map(int, input().split())
sumt = sum(t)

sv = [0]
for i in range(N):
    for j in range(t[i]*2):
        sv.append(v[i])
sv.append(0)

# dp[i][j] := i/2秒後に速度がj/2のときの最大距離
dp = [[-float('inf')]*201 for _ in range(sumt*2+1)]
dp[0][0] = 0
for i in range(1, len(dp)):
    maxj = min(sv[i], sv[i+1])*2
    for j in range(len(dp[i])):
        k = 0.25*j
        # 変化なし
        if j <= maxj:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+k)
        # 加速
        if (j+1) <= maxj:
            dp[i][j+1] = max(dp[i][j+1], dp[i-1][j]+k+0.25)
        # 減速
        if j > 0 and (j-1) <= maxj:
            dp[i][j-1] = max(dp[i][j-1], dp[i-1][j]+k-0.25)

print(dp[-1][0])
