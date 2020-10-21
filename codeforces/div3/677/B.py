for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    l, r = 0, n-1
    while l < n and a[l] == 0:
        l += 1
    while r >= 0 and a[r] == 0:
        r -= 1
    l = min(l, n-1)
    r = max(0, r)
    ans = 0
    for i in range(l, r+1):
        if a[i] == 0:
            ans += 1
    print(ans)
