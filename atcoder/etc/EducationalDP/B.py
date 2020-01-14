N, K = map(int, input().split())
*h, = map(int, input().split())

dp = [0] * N
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    c = 10**10
    for j in range(i - 1, max(i - K - 1, -1), -1):
        t = abs(h[j] - h[i]) + dp[j]
        if t < c:
            c = t
    dp[i] = c
print(dp[N - 1])
