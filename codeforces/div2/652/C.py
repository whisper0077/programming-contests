import bisect
for t in range(int(input())):
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    *w, = map(int, input().split())
    a.sort()
    w.sort()

    ans = 0
    l, r = 0, n-1

    i = 0
    while i < len(w) and w[i] == 1:
        ans += a[r]*2
        r -= 1
        i += 1

    i = len(w)-1
    while i >= 0 and w[i] > 1:
        ans += a[l]+a[r]
        l += w[i]-1
        r -= 1
        i -= 1
    print(ans)
