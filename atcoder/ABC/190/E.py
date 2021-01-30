from collections import defaultdict, deque
import sys
input = sys.stdin.readline
INF = 10**10

N, M = map(int, input().split())
g = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

K = int(input())
*c, = map(int, input().split())

kg = [[] for _ in range(K)]
for i in range(K):
    q = deque([c[i]])
    w = [INF]*(N+1)
    w[c[i]] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if w[v] == INF:
                w[v] = w[u]+1
                q.append(v)
    kg[i] = [w[c[j]] for j in range(K)]

dp = [[INF]*K for _ in range(2**K)]
for i in range(K):
    dp[1 << i][i] = 1

for s in range(2**K):
    for u in range(K):
        for v in range(K):
            if s & (1 << v) == 0:
                dp[s | (1 << v)][v] = min(dp[s | (1 << v)][v], dp[s][u]+kg[u][v])

ans = min(dp[-1])
if ans == INF:
    print(-1)
else:
    print(ans)
