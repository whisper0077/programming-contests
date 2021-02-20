import heapq
INF = 10**20


def dijkstra(g, s):
    n = len(g)
    d = [INF]*n
    d[s] = 0
    q = [(0, s)]
    while q:
        c, u = heapq.heappop(q)
        if d[u] < c:
            continue
        for v, t, k in g[u]:
            nc = (d[u]+k-1)//k * k + t
            if nc < d[v]:
                d[v] = nc
                heapq.heappush(q, (d[v], v))
    return d


N, M, X, Y = map(int, input().split())
g = [[] for i in range(N)]
for i in range(M):
    a, b, t, k = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append((b, t, k))
    g[b].append((a, t, k))

d = dijkstra(g, X-1)
ans = d[Y-1]
if ans == INF:
    ans = -1
print(ans)
