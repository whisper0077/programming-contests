for _ in range(int(input())):
    n = int(input())
    *x, = map(int, input().split())
    d = [False]*(2*n+2)
    for v in x:
        if not d[v]:
            d[v] = True
        else:
            d[v+1] = True
    print(d.count(True))
