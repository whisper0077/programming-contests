def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def extgcd(a, b):
    '''
    拡張ユークリッド互除法
    ax + by = gcd(a,b) = d
    d,x,yを求める
    '''

    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0


def modinv(a, p):
    '''
    extgcdを用いた、ax ≡ 1 mod pとなるxを求める（aの逆元）
    '''
    g, x, y = extgcd(a, p)
    if g != 1:
        return -1
    else:
        # xは負の可能性がある
        return x % p


if __name__ == "__main__":
    print(gcd(6, 12))
    print(lcm(2, 3))
    for i in range(1, 13):
        print(modinv(i, 13))
