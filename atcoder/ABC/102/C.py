N = int(input())
*a, = map(int, input().split())
if N == 1:
    print(0)
else:
    b = [a[i]-i-1 for i in range(N)]
    b.sort()
    if N % 2 == 0:
        m = [b[N//2-1], b[N//2]]
    else:
        m = [b[N//2]]

    ans = 10**18
    for v in m:
        t = sum([abs(b[i]-v) for i in range(N)])
        ans = min(t, ans)
    print(ans)
