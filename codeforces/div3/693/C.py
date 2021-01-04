for t in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    a = [0]+a
    v = [0]*(n+1)
    for i in range(n, 0, -1):
        ta = 0
        j = i
        while j <= n:
            if v[j] != 0:
                ta += v[j]
                break
            ta += a[j]
            j += a[j]
        v[i] = ta
    print(max(v))
