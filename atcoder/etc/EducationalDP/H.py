mod = (10**9)+7

H, W = map(int, input().split())
a = ["#"+input().strip()+"#" for _ in range(H)]
a = ["#"*(W+2)] + a + ["#"*(W+2)]
a[1] = "."+a[1][1:]

dp = [[0]*(W+2) for _ in range(H+2)]
dp[1][0] = 1

for y in range(1, H+1):
    for x in range(1, W+1):
        if a[y][x] == '.':
            t = 0
            if a[y][x-1] == '.':
                t += dp[y][x-1]
            if a[y-1][x] == '.':
                t += dp[y-1][x]
            dp[y][x] = t % mod
print(dp[H][W])
