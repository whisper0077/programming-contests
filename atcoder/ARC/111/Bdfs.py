n = int(input())
g = [[] for _ in range(400000)]
nmax = 0
for i in range(n):
    a, b = map(int, input().split())
    nmax = max(nmax, a, b)
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

used = [0]*nmax


def dfs(v, p):
    if used[v] == 1:
        return True

    if p != -1:
        used[v] = 1

    cycle = False
    for u in g[v]:
        if u != p:
            cycle = dfs(u, v) or cycle

    if cycle:
        used[v] = 1

    return cycle


for i in range(nmax):
    dfs(i, -1)

print(sum(used))
