n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    u, k, *v, = map(int, input().split())
    for vi in v:
        g[u][vi] = 1

d = [-1]*(n+1)
d[1] = 0

l = [1]
while len(l) > 0:
    u = l.pop(0)
    for i, v in enumerate(g[u]):
        if v == 1 and d[i] < 0:
            d[i] = d[u]+1
            l.append(i)

for i in range(1, n+1):
    print(f"{i} {d[i]}")
