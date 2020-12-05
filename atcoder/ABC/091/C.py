N = int(input())
r = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

r.sort()
b.sort()

ans = 0
for i in range(N):
    bx, by = b[i]
    my = -1
    k = -1
    for j in range(N):
        rx, ry = r[j]
        if (bx-rx) > 0 and (by-ry) > 0:
            if ry > my:
                k = j
                my = ry

    if k != -1:
        ans += 1
        r[k] = [999, 999]
print(ans)
