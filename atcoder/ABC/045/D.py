N = int(input())
dp = [[0]*(N+2) for _ in range(N+2)]
dp[0][1] = 1
S = ["."+input()+"." for _ in range(N)]
S = ["."*(N+2)]+S+["."*(N+2)]
for y in range(1, N+1):
    for x in range(1, N+1):
        if S[y][x] == ".":
            dp[y][x] = dp[y-1][x]+dp[y][x-1]
print(dp[N][N])
