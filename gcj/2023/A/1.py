for t in range(int(input())):
    d = input().split()
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m = {}
    for i in range(len(a)):
        m[a[i]] = d[i]
    n = int(input())
    cm = {}
    ans = "NO"
    for i in range(n):
        s = input()
        k = "".join([m[si] for si in s])
        if k in cm:
            ans = "YES"
        cm[k] = True

    print("Case #{}: {}".format(t+1, ans))
