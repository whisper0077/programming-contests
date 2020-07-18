from collections import deque


def topoSort(g):
    n = len(g)
    inedges = [0]*n
    for i in range(n):
        for v in g[i]:
            inedges[v] += 1

    q = deque()
    for i in range(n):
        if inedges[i] == 0:
            q.append(i)

    r = []
    while q:
        v = q.popleft()
        r.append(v)
        for u in g[v]:
            inedges[u] -= 1
            if inedges[u] == 0:
                q.append(u)
    return r


for t in range(int(input())):
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    e = []
    h = {}
    for i in range(m):
        t, x, y = map(int, input().split())
        x -= 1
        y -= 1
        if t == 1:
            g[x].append(y)
        e.append([x, y])
        h[x] = True
        h[y] = True

    a = topoSort(g)
    if len(a) != n:
        print("NO")
        continue

    p = [0]*n
    for i in range(n):
        p[a[i]] = i

    print("YES")
    for x, y in e:
        if p[x] < p[y]:
            print(x+1, y+1)
        else:
            print(y+1, x+1)
