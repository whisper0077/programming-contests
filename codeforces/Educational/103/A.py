for t in range(int(input())):
    n, k = map(int, input().split())
    m = (n+k-1)//k
    k *= m
    print((k+n-1)//n)
