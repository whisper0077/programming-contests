import bisect
H, W, N, M = map(int, input().split())
g = [[0]*W for _ in range(H)]
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a][b] = 1
for i in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    g[c][d] = -1

wl = [[] for _ in range(H)]
hl = [[] for _ in range(W)]
for y in range(H):
    wl[y].append((-1, 0))
    for x in range(W):
        if g[y][x] != 0:
            wl[y].append((x, g[y][x]))
    wl[y].append((2000, 0))
for x in range(W):
    hl[x].append((-1, 0))
    for y in range(H):
        if g[y][x] != 0:
            hl[x].append((y, g[y][x]))
    hl[x].append((2000, 0))


ans = 0
for y in range(H):
    for x in range(W):
        if g[y][x] == 0:
            xi = bisect.bisect_left(wl[y], (x, 0))
            xi1, xv1 = wl[y][xi-1]
            xi2, xv2 = wl[y][xi]

            yi = bisect.bisect_left(hl[x], (y, 0))
            yi1, yv1 = hl[x][yi-1]
            yi2, yv2 = hl[x][yi]
            if xv1 == 1 or xv2 == 1 or yv1 == 1 or yv2 == 1:
                g[y][x] = 1

        if g[y][x] == 1:
            ans += 1
print(ans)
