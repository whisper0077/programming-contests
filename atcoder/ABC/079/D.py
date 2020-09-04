N = 10
H, W = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(H)]
for h in range(N):
    for w in range(N):
        if g[h][w] == 0:
            g[h][w] = float('inf')

for k in range(N):
    for i in range(N):
        for j in range(N):
            g[i][j] = min(g[i][j], g[i][k]+g[k][j])

ans = 0
for h in range(H):
    for w in range(W):
        if abs(A[h][w]) != 1:
            ans += g[A[h][w]][1]

print(ans)
