def isqrt(n):
    '''
    ニュートン法による整数の平方根
    '''
    if n == 0:
        return 0
    x = 1 << (n.bit_length() + 1) // 2
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def ceil(n, d):
    # return -(-n//d)
    return (n+d-1)//d


def floor(n, d):
    return n//d
