import heapq

# 隣接リスト式で保持
n = int(input())
g = [[] for i in range(n)]
for i in range(n):
    u, k, *l, = map(int, input().split())
    for j in range(k):
        v, c = l[j*2], l[j*2+1]
        g[u].append([v, c])

'''
ダイクストラ法による単一始点最短経路
隣接リスト+二分ヒープ（優先度付きキュー）による高速化
'''
d = [2**64]*n
d[0] = 0
h = []
heapq.heappush(h, (0, 0))

m = [False]*n
while len(h) > 0:
    c, u = heapq.heappop(h)
    m[u] = True
    if d[u] < c:
        continue
    for gv, gc in g[u]:
        if not m[gv] and d[u]+gc < d[gv]:
            d[gv] = d[u]+gc
            heapq.heappush(h, (d[u]+gc, gv))

for i in range(n):
    print(f"{i} {d[i]}")
