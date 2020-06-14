X, N = map(int, input().split())
if N == 0:
    print(X)
else:
    *p, = map(int, input().split())
    ans = -1
    d = 10**10
    for i in range(-101, 102):
        if i in p:
            continue
        m = abs(i-X)
        if m < d:
            d = m
            ans = i
    print(ans)
