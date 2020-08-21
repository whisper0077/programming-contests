for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    d = min(a)

    b = []
    for i in range(n):
        if a[i] % d == 0:
            b.append(a[i])
    b.sort()

    ans = "YES"
    bi = 0
    m = 0
    for i in range(n):
        if a[i] % d == 0:
            if b[bi] < m:
                ans = "NO"
                break
            m = b[bi]
            bi += 1
        else:
            if a[i] < m:
                ans = "NO"
                break
            m = a[i]
    print(ans)
