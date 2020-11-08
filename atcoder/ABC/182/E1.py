import bisect
H, W, N, M = map(int, input().split())
g = [[0]*W for _ in range(H)]
l = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
    l.append((a, b))
for i in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    g[c][d] = -1

for y, x in l:
    for i in range(x+1, W):
        if g[y][i] == -1 or g[y][i] == 1:
            break
        g[y][i] = 2
    for i in range(x-1, -1, -1):
        if g[y][i] == -1 or g[y][i] == 1:
            break
        g[y][i] = 2
    for i in range(y+1, H):
        if g[i][x] == -1 or g[i][x] == 1:
            break
        g[i][x] = 2
    for i in range(y-1, -1, -1):
        if g[i][x] == -1 or g[i][x] == 1:
            break
        g[i][x] = 2

ans = 0
for y in range(H):
    for x in range(W):
        if g[y][x] > 0:
            ans += 1
print(ans)
