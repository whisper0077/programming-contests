from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

h = defaultdict(list)
for i in range(M):
    x, y = map(int, input().split())
    h[x-1].append(y-1)

dp = [0]*N


def dist(v):
    if dp[v] > 0:
        return dp[v]
    dp[v] = 0
    for nv in h[v]:
        dp[v] = max([dp[v], dist(nv)+1])
    return dp[v]


ans = 0
for v in range(N):
    ans = max([ans, dist(v)])

print(ans)
