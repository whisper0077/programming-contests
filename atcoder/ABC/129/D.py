h, w = map(int, input().split())
m = [input().strip() for _ in range(h)]

l = [[0] * w for _ in range(h)]
r = [[0] * w for _ in range(h)]
u = [[0] * w for _ in range(h)]
d = [[0] * w for _ in range(h)]

for y in range(h):
    for x in range(w):
        dy = y
        uy = h - y - 1
        if m[dy][x] == '.':
            if dy == 0:
                d[dy][x] = 1
            else:
                d[dy][x] = d[dy - 1][x] + 1
        if m[uy][x] == '.':
            if uy == (h - 1):
                u[uy][x] = 1
            else:
                u[uy][x] = u[uy + 1][x] + 1

        lx = x
        rx = w - x - 1
        if m[y][lx] == '.':
            if lx == 0:
                l[y][lx] = 1
            else:
                l[y][lx] = l[y][lx - 1] + 1
        if m[y][rx] == '.':
            if rx == (w - 1):
                r[y][rx] = 1
            else:
                r[y][rx] = r[y][rx + 1] + 1

ans = 0
for y in range(h):
    for x in range(w):
        t = l[y][x] + r[y][x] + u[y][x] + d[y][x] - 3
        if t > ans:
            ans = t
print(ans)