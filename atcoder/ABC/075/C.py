from collections import deque

N, M = map(int, input().split())
g = [[] for _ in range(N)]
e = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    e.append([a, b])

ans = 0
for i, j in e:
    used = {}
    q = deque([0])
    while q:
        u = q.popleft()
        for v in g[u]:
            if (v in used) or (i == u and j == v) or (i == v and j == u):
                continue
            else:
                q.append(v)
                used[v] = True
    if len(used) < N:
        ans += 1
print(ans)
