N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for a, b in ab:
    ans = -1
    m = 10**9
    i = 1
    for c, d in cd:
        t = abs(c-a)+abs(d-b)
        if t < m:
            m = t
            ans = i
        i += 1
    print(ans)
