for _ in range(int(input())):
    n = int(input())
    *x, = map(int, input().split())
    h = {}
    for i in range(n-1):
        for j in range(i+1, n):
            h[x[j]-x[i]] = True
    print(len(h))
