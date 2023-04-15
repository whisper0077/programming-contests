a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for t in range(int(input())):
    n = int(input())-1
    ans = a[n % 26]
    if n >= 26:
        l, r = 1, 10**100
        while (r-l) > 1:
            m = (l+r)//2
            v = 26 * m*(m+1)//2
            if n >= v:
                l = m
            else:
                r = m
        p = n-l*r*26//2
        ans = a[p//r]

    print("Case #{}: {}".format(t+1, ans))
