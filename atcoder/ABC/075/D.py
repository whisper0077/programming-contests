import itertools
N, K = map(int, input().split())
xy = []
x, y = [], []
for i in range(N):
    a, b = map(int, input().split())
    xy.append([a, b])
    x.append(a)
    y.append(b)

ans = float('inf')
for sx, ex in itertools.combinations(x, 2):
    for sy, ey in itertools.combinations(y, 2):
        if ex < sx:
            sx, ex = ex, sx
        if ey < sy:
            sy, ey = ey, sy
        s = (ex-sx)*(ey-sy)
        if s == 0:
            continue

        c = 0
        for k in range(N):
            a, b = xy[k]
            if sx <= a and a <= ex and sy <= b and b <= ey:
                c += 1
        if c >= K and s < ans:
            ans = s

print(ans)
