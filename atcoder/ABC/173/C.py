H, W, K = map(int, input().split())
c = [list(input().strip()) for _ in range(H)]
b = 0
for y in range(H):
    for x in range(W):
        if c[y][x] == "#":
            b += 1

ans = 0
for row in range(2 ** H):
    rows = []
    for h in range(H):
        if row & (1 << h):
            rows.append(h)
    for col in range(2 ** W):
        rc = {}
        cols = []
        for w in range(W):
            if col & (1 << w):
                cols.append(w)

        for y in rows:
            for x in range(W):
                rc[(y, x)] = c[y][x]
        for x in cols:
            for y in range(H):
                rc[(y, x)] = c[y][x]

        tb = b
        for v in rc.values():
            if v == "#":
                tb -= 1
        if tb == K:
            ans += 1
print(ans)
