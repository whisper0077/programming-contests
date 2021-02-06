import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = 10**18


def dijkstra(g, s):
    n = len(g)
    d = [INF]*n
    d[s] = 0
    q = [(0, s)]
    while q:
        c, u = heapq.heappop(q)
        if d[u] < c:
            continue
        for v, nc in g[u]:
            if (d[u]+nc) < d[v]:
                d[v] = d[u]+nc
                heapq.heappush(q, (d[v], v))
    return d


N, M = map(int, input().split())
g = [[] for _ in range(N)]
sames = [INF]*N
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if a == b:
        sames[a] = min(sames[a], c)
    else:
        g[a].append((b, c))

d = [[]]*N
for i in range(N):
    d[i] = dijkstra(g, i)

for i in range(N):
    ans = INF
    for j in range(N):
        if i == j:
            ans = min(ans, sames[i])
        else:
            ans = min(ans, d[i][j]+d[j][i])
    if ans == INF:
        ans = -1
    print(ans)
