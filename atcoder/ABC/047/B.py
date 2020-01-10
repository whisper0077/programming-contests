W, H, N = map(int, input().split())
sx, sy, ex, ey = 0, 0, W, H
for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        sx = max([x, sx])
    elif a == 2:
        ex = min([x, ex])
    elif a == 3:
        sy = max([y, sy])
    else:
        ey = min([y, ey])

w, h = ex-sx, ey-sy
if w < 0 or h < 0:
    print(0)
else:
    print((ex-sx)*(ey-sy))
