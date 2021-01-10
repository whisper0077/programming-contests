import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
*A, = map(int, input().split())
g = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    g[x-1].append(y-1)

used = [-float('inf')]*N
ans = -float('inf')


def dfs(v):
    global ans
    if used[v] != -float('inf'):
        return used[v]
    ny = -float('inf')
    if len(g[v]) > 0:
        by = A[v]
        ny = 0
        for u in g[v]:
            ny = max(ny, dfs(u), A[u])
        #print("buy", v, by, ny)
        ans = max(ans, ny-by)
        used[v] = ny
    return ny


for i in range(N):
    if used[i] == -float('inf'):
        dfs(i)

print(ans)
