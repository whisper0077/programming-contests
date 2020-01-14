N = int(input())
*h, = map(int, input().split())

dp = [0] * N
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    c1, c2 = abs(h[i - 1] - h[i]) + dp[i - 1], abs(h[i - 2] - h[i]) + dp[i - 2]
    if c1 < c2:
        dp[i] = c1
    else:
        dp[i] = c2

print(dp[N - 1])
