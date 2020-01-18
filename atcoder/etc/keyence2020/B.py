N = int(input())
r = [list(map(int, input().split())) for _ in range(N)]
r.sort()

l = r[0]
ri = 1
ans = N
while ri < N:
    x1, l1 = l
    x2, l2 = r[ri]
    if (x1+l1) > (x2-l2):
        if (x1+l1) > (x2+l2):
            l = r[ri]
            ri += 1
        else:
            ri += 1
        ans -= 1
    else:
        l = r[ri]
        ri += 1
print(ans)
