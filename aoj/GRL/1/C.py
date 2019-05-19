v, e = map(int, input().split())
inf = 2**32
dp = [[inf for _ in range(v)] for _ in range(v)]

'''
ワーシャルフロイドのアルゴリズム
動的計画法
重み付き有向グラフの全点対間最短経路の距離
'''
for i in range(v):
    dp[i][i] = 0

for i in range(e):
    s, t, d = map(int, input().split())
    dp[s][t] = d

for k in range(v):
    for i in range(v):
        if dp[i][k] >= inf:
            continue
        for j in range(v):
            if dp[k][j] >= inf:
                continue
            dp[i][j] = min([dp[i][j], dp[i][k]+dp[k][j]])

negative = False
for i in range(v):
    if dp[i][i] < 0:
        negative = True
        break

if negative:
    print("NEGATIVE CYCLE")
else:
    for i in range(v):
        ans = []
        for j in range(v):
            if dp[i][j] >= inf:
                ans.append("INF")
            else:
                ans.append(str(dp[i][j]))
        print(" ".join(ans))
