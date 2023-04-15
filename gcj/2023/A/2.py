for t in range(int(input())):
    m, r, n = map(int, input().split())
    *x, = map(int, input().split())
    xi = -1
    mi = 0
    ans = 0
    while mi < m:
        pi = xi
        while (xi+1) < n and (x[xi+1]-r) <= mi and mi <= (x[xi+1]+r):
            xi += 1

        if pi != xi:
            ans += 1
            mi = x[xi]+r
        else:
            break

    if mi < m:
        ans = "IMPOSSIBLE"
    print("Case #{}: {}".format(t+1, ans))
