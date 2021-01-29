for t in range(int(input())):
    n, k = map(int, input().split())
    *p, = map(int, input().split())

    l, r = 10**18, -1
    while abs(l-r) > 1:
        m = (r+l)//2
        ok = True
        b = p[0]+m
        for i in range(1, n):
            a = p[i]*100
            if a > b*k:
                ok = False
                break
            b += p[i]
        if ok:
            l = m
        else:
            r = m
    print(l)
