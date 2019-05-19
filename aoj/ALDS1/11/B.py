n = int(input())
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    u, k, *v, = map(int, input().split())
    for vi in v:
        g[u][vi] = 1

d = [0]*(n+1)
f = [0]*(n+1)
t = 0


def dfs(u):
    global t
    if d[u] != 0:
        return
    t += 1
    d[u] = t
    for i, v in enumerate(g[u]):
        if v == 1:
            dfs(i)
    t += 1
    f[u] = t


for i in range(1, n+1):
    if d[i] == 0:
        dfs(i)
for i in range(1, n+1):
    print(f"{i} {d[i]} {f[i]}")
