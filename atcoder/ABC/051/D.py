import copy
N, M = map(int, input().split())
dp = [[float('inf')]*N for _ in range(N)]
ms = []
for i in range(N):
    dp[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
    ms.append([a-1, b-1, c])

g = copy.deepcopy(dp)

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min([dp[i][j], dp[i][k]+dp[k][j]])

# 全頂点でmが使われたかどうか
ans = M
for m in ms:
    a, b, c = m
    for n in range(N):
        if dp[n][b] == (dp[n][a]+c):
            ans -= 1
            break
print(ans)
