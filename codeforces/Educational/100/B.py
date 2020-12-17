for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    s = sum(a)
    ans = []
    for i in range(n):
        m, v = 2**31, 0
        for j in range(30):
            d = abs(a[i]-2**j)
            if d < m:
                m, v = d, 2**j
        ans.append(v)
    print(*ans)
