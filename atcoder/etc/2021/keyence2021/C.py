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
dp[0][0] = pow(3, H*W-K, MOD)
inv3 = 332748118  # pow(3, -1, MOD)

'''
配るDP
'''
for y in range(H):
    for x in range(W):
        if m[y][x] == -1:
            d = dp[y][x]*inv3*2 % MOD
            dp[y][x+1] += d
            dp[y+1][x] += d
        else:
            if m[y][x] != 0:
                dp[y+1][x] += dp[y][x]
            if m[y][x] != 1:
                dp[y][x+1] += dp[y][x]
        dp[y][x+1] %= MOD
        dp[y+1][x] %= MOD

'''
もらうDP
for y in range(H):
    for x in range(W):
        if x > 0:
            xd = 0
            if m[y][x-1] == -1:
                xd = dp[y][x-1]*inv3*2 % MOD
            elif m[y][x-1] != 1:
                xd = dp[y][x-1]
            dp[y][x] += xd
        if y > 0:
            yd = 0
            if m[y-1][x] == -1:
                yd = dp[y-1][x]*inv3*2 % MOD
            elif m[y-1][x] != 0:
                yd = dp[y-1][x]
            dp[y][x] += yd
        dp[y][x] %= MOD
'''

print(dp[H-1][W-1])
