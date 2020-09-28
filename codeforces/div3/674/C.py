for t in range(int(input())):
    n = int(input())
    p = n-1
    for i in range(2, int(n**0.5+1)):
        m = (n+i-1)//i-1
        q = i-1+m
        if q < p:
            p = q
    print(p)
