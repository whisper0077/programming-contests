for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    s = list(sorted(a))
    l, r = 0, n-1
    while l < n and a[l] == s[l]:
        l += 1
    while r >= 0 and a[r] == s[r]:
        r -= 1

    if l < r:
        r += 1
        ans = 1
        for i in range(l, r):
            if a[i] == s[i]:
                ans = 2
                break
        print(ans)
    else:
        print(0)
