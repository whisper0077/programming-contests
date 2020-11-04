H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

h = {}
for y in range(H):
    for x in range(W):
        h[A[y][x]] = (x, y)

d = [0]*(H*W+1)
for i in range(1, D+1):
    for j in range(i+D, H*W+1, D):
        s, e = j-D, j
        sx, sy = h[s]
        ex, ey = h[e]
        d[e] = d[s]+abs(sx-ex)+abs(sy-ey)

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(d[r]-d[l])
