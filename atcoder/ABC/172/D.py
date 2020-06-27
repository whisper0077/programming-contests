N = int(input())
dp = [1]*(N+1)
ans = 1
for i in range(2, N+1):
    j = i
    while j < N+1:
        dp[j] += 1
        j += i
    ans += i*dp[i]
print(ans)
