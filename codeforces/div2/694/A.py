for t in range(int(input())):
    n, x = map(int, input().split())
    *a, = map(int, input().split())
    minv = (sum(a)+x-1)//x
    maxv = 0
    for v in a:
        maxv += (v+x-1)//x
    print(minv, maxv)
