
N = int(input())
abc = [list(map(int, input().split())) for i in range(N)]
abc.append([0, 0, 0])

dp = [[-1] * 4 for i in range(N + 1)]
dp[0] = [0, 0, 0]
for i in range(1, N + 1):
    dp[i][0] = max([dp[i - 1][1] + abc[i - 1][1], dp[i - 1][2] + abc[i - 1][2]])
    dp[i][1] = max([dp[i - 1][0] + abc[i - 1][0], dp[i - 1][2] + abc[i - 1][2]])
    dp[i][2] = max([dp[i - 1][1] + abc[i - 1][1], dp[i - 1][0] + abc[i - 1][0]])

print(max(dp[N]))

'''全探索
def happy(n, p):
    if n < 0:
        return 0
    if dp[n][p] >= 0:
        return dp[n][p]

    a = 0 if p == 0 else happy(n - 1, 0) + abc[n][0]
    b = 0 if p == 1 else happy(n - 1, 1) + abc[n][1]
    c = 0 if p == 2 else happy(n - 1, 2) + abc[n][2]
    dp[n][p] = max([a, b, c])

    return dp[n][p]
'''