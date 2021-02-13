for t in range(int(input())):
    l, r = map(int, input().split())
    if (r-l) < l:
        print(0)
    else:
        n = r-2*l+1
        print(n*(n+1)//2)
