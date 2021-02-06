def isqrt(n):
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def ceil(n, d):
    # return -(-n//d)
    return (n+d-1)//d


def floor(n, d):
    return n//d
