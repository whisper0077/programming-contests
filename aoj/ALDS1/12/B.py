n = int(input())
g = [[2**64]*n for i in range(n)]
for i in range(n):
    u, k, *l, = map(int, input().split())
    for j in range(k):
        v, c = l[j*2], l[j*2+1]
        g[u][v] = c

'''
ダイクストラ法による単一始点最短経路
負の重みをもつグラフには適用できない
'''
d = [2**64]*n
d[0] = 0

s = []
v = [i for i in range(n)]
while len(s) < n:
    c, u = 2**32, -1
    for vv in v:
        if d[vv] < c:
            c, u = d[vv], vv
    s.append(u)
    v.remove(u)
    for i, c in enumerate(g[u]):
        if i in v and d[u]+g[u][i] < d[i]:
            d[i] = d[u]+g[u][i]

for i in range(n):
    print(f"{i} {d[i]}")
