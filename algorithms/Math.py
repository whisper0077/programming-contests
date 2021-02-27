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


def crt(r, m):
    '''
    |r|==|m|の中国剰余定理
    r[i] ≡ x (mod m[i])
    となるxとlcmを求める
    '''
    if len(r) != len(m):
        return (0, 0)
    r0, m0 = 0, 1
    for i in range(len(r)):
        # m0*x + m1*y = gcd(m0, m1)
        # m0*x ≡ gcd(m0, m1) (mod m1)
        d, x, y = extgcd(m0, m[i])
        if (r[i]-r0) % d != 0:
            return (0, 0)

        u = m0 * m[i]//d  # lcm(m0, m1)
        r0 += (r[i]-r0)//d * m0 * x % u
        m0 = u
    return (r0, m0)


def modinv(a, p):
    '''
    extgcdを用いた、ax ≡ 1 (mod p)となるxを求める（aの逆元）
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
    print(crt([2, 3], [3, 5]))
