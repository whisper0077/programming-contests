import sys
input = sys.stdin.readline

MOD = 998244353
H, W, K = map(int, input().split())
m = [[-1]*W for _ in range(H)]
ci = {'R': 0, 'D': 1, 'X': 2}
for i in range(K):
    h, w, c = input().split()
    h = int(h)-1
    w = int(w)-1
    m[h][w] = ci[c]

dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][0] = 1
inv3 = 332748118  # pow(3, -1, MOD)
inv3m2 = inv3*2
for y in range(H):
    for x in range(W):
        dp[y][x] %= MOD
        if m[y][x] == -1:
            dp[y][x+1] += dp[y][x]*inv3m2
            dp[y+1][x] += dp[y][x]*inv3m2
        elif m[y][x] == 0:
            dp[y][x+1] += dp[y][x]
        elif m[y][x] == 1:
            dp[y+1][x] += dp[y][x]
        else:
            dp[y][x+1] += dp[y][x]
            dp[y+1][x] += dp[y][x]

print(dp[H-1][W-1]*pow(3, H*W-K, MOD) % MOD)
