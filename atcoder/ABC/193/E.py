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
        d, x, y = extgcd(m0, m[i])
        if (r[i]-r0) % d != 0:
            return (0, 0)

        u = m[i]//d
        tmp = (r[i]-r0)//d * x % u
        r0 += m0*tmp
        m0 *= u
    return (r0, m0)


INF = 10**20
for t in range(int(input())):
    '''
    t mod (2X+2Y) = t1 -> t ≡ t1 (mod (2X+2Y))
    t mod (P+Q) = t2   -> t ≡ t2 (mod (P+Q))
    '''
    x, y, p, q = map(int, input().split())
    ans = INF
    for t1 in range(x, x+y):
        for t2 in range(p, p+q):
            m, d = crt([t1, t2], [2*x+2*y, p+q])
            if d > 0:
                ans = min(m, ans)
    if ans == INF:
        ans = "infinity"
    print(ans)
