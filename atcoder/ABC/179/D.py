MOD = 998244353
N, K = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(K)]
lr.sort()

# 考え方は通常のDPだが、そのままだとO(N^2)となる
# 独立した区間なので、区間の和を求める部分の計算量を落とせば良い(dpsumで累積和を計算)
dp = [0]*(N+1)
dp[1] = 1

dpsum = [0]*(N+1)
dpsum[1] = 1

for i in range(2, N+1):
    for l, r in lr:
        li = max(0, i-r)
        ri = i-l
        if ri < 0:
            continue
        dp[i] += dpsum[ri]-dpsum[li-1]
        dp[i] %= MOD
    dpsum[i] += dp[i]+dpsum[i-1]
    dpsum[i] %= MOD

print(dp[N])
