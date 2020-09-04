for t in range(int(input())):
    n, s = map(int, input().split())
    m = n
    ans = n
    d = 0
    while True:
        a = m
        c = 0
        while a > 0:
            c += a % 10
            a //= 10
        if c <= s:
            ans = m*(10**d)-n
            break
        if m % 10 == 0:
            m //= 10
            d += 1
        else:
            m += 10-m % 10
    print(ans)
